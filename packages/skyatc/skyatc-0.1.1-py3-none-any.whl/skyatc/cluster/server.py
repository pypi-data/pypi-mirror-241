import json
import time
import uuid
import configparser
import yaml
import logging
import os
import socket
from contextlib import closing
from enum import Enum, auto
from functools import partial
from pathlib import Path

import urllib3
from typing import Dict, Optional, Tuple, List

# from skyplane import compute
# from skyplane.compute.const_cmds import make_autoshutdown_script, make_dozzle_command, make_sysctl_tcp_tuning_command
from skyplane.config_paths import __config_root__
from skyplane.utils import logger
from skyplane.utils.fn import PathLike, wait_for
import skyplane.compute

# from skyplane.utils.retry import retry_backoff
from skyplane.utils.timer import Timer

tmp_log_dir = Path("/tmp/skyplane")


class ServerType(Enum):
    CONTROLLER = auto()
    WORKER = auto()


class ServerState(Enum):
    PENDING = auto()
    RUNNING = auto()
    SUSPENDED = auto()
    TERMINATED = auto()
    UNKNOWN = auto()

    def __str__(self):
        return self.name.lower()

    @staticmethod
    def from_gcp_state(gcp_state):
        mapping = {
            "PROVISIONING": ServerState.PENDING,
            "STAGING": ServerState.PENDING,
            "RUNNING": ServerState.RUNNING,
            "REPAIRING": ServerState.RUNNING,
            "SUSPENDING": ServerState.SUSPENDED,
            "SUSPENDED": ServerState.SUSPENDED,
            "STOPPING": ServerState.TERMINATED,
            "TERMINATED": ServerState.TERMINATED,
        }
        return mapping.get(gcp_state, ServerState.UNKNOWN)

    @staticmethod
    def from_azure_state(azure_state):
        mapping = {
            "PowerState/starting": ServerState.PENDING,
            "PowerState/running": ServerState.RUNNING,
            "PowerState/stopping": ServerState.SUSPENDED,
            "PowerState/stopped": ServerState.SUSPENDED,
            "PowerState/deallocating": ServerState.TERMINATED,
            "PowerState/deallocated": ServerState.TERMINATED,
        }
        return mapping.get(azure_state, ServerState.UNKNOWN)

    @staticmethod
    def from_aws_state(aws_state):
        mapping = {
            "pending": ServerState.PENDING,
            "running": ServerState.RUNNING,
            "shutting-down": ServerState.TERMINATED,
            "terminated": ServerState.TERMINATED,
            "stopping": ServerState.SUSPENDED,
            "stopped": ServerState.SUSPENDED,
        }
        return mapping.get(aws_state, ServerState.UNKNOWN)

    @staticmethod
    def from_ibmcloud_state(ibmcloud_state):
        mapping = {
            "pending": ServerState.PENDING,
            "running": ServerState.RUNNING,
            "shutting-down": ServerState.TERMINATED,
            "terminated": ServerState.TERMINATED,
            "stopping": ServerState.SUSPENDED,
            "stopped": ServerState.SUSPENDED,
        }
        return mapping.get(ibmcloud_state, ServerState.UNKNOWN)


class Server:
    """Abstract server class to support basic SSH operations"""

    def __init__(
        self,
        region_tag: str,
        type: ServerType,
        instance_name: Optional[str] = None,
        log_dir=None,
        # image_family: str,
        # instance_type: str,
        # boot_disk_size_gb: Optional[int] = 10,
        # auto_shutdown_timeout_minutes: Optional[int] = None
    ):
        self.region_tag = region_tag  # format provider:region
        self.type = type
        self.auto_shutdown_timeout_minutes = 15

        if instance_name is None:
            if self.type == ServerType.CONTROLLER:
                self.instance_name = f"controller-{str(uuid.uuid4().hex[:8])}"
            else:
                self.instance_name = f"worker-{str(uuid.uuid4().hex[:8])}"
        else:
            self.instance_name = instance_name
        print("INSTANCE NAME", self.instance_name)

        self.command_log = []
        self.gateway_log_viewer_url = None
        self.gateway_api_url = None
        self.init_log_files(log_dir)
        self.ssh_tunnels: Dict = {}
        self._ssh_client = None

    def __repr__(self):
        return f"Server({self.uuid()})"

    def __hash__(self):
        return hash((self.region_tag, self.uuid()))

    def uuid(self):
        raise NotImplementedError()

    def init_log_files(self, log_dir):
        if log_dir:
            log_dir = Path(log_dir)
            log_dir.mkdir(parents=True, exist_ok=True)
            self.command_log_file = str(log_dir / f"{self.uuid()}.jsonl")
        else:
            self.command_log_file = None

    def get_sftp_client(self):
        raise NotImplementedError()

    def get_ssh_client_impl(self):
        raise NotImplementedError()

    def open_ssh_tunnel_impl(self, remote_port):
        raise NotImplementedError()

    def get_ssh_cmd(self) -> str:
        raise NotImplementedError()

    def install_nvidia_drivers(self):
        raise NotImplementedError()

    @property
    def ssh_client(self):
        """Create SSH client and cache."""
        if not self._ssh_client:
            self._ssh_client = self.get_ssh_client_impl()
        return self._ssh_client

    def tunnel_port(self, remote_port: int) -> int:
        """Returns a local port that tunnels to the remote port."""
        if remote_port not in self.ssh_tunnels:

            def start():
                tunnel = self.open_ssh_tunnel_impl(remote_port)
                tunnel.start()
                tunnel._check_is_started()
                return tunnel

            self.ssh_tunnels[remote_port] = retry_backoff(start)
        local_bind_port = self.ssh_tunnels[remote_port].local_bind_port
        logger.fs.debug(
            f"Bound remote port {self.uuid()}:{remote_port} to localhost:{local_bind_port}"
        )
        return local_bind_port

    @property
    def provider(self) -> str:
        """Format provider"""
        return self.region_tag.split(":")[0]

    def instance_state(self) -> ServerState:
        raise NotImplementedError()

    def public_ip(self):
        raise NotImplementedError()

    def private_ip(self):
        raise NotImplementedError()

    def instance_class(self):
        raise NotImplementedError()

    def region(self):
        """Per-provider region e.g. us-east-1"""
        raise NotImplementedError()

    def instance_name(self):
        raise NotImplementedError()

    def tags(self):
        raise NotImplementedError()

    def network_tier(self):
        raise NotImplementedError()

    def terminate_instance_impl(self):
        raise NotImplementedError()

    def terminate_instance(self):
        """Terminate instance"""
        self.close_server()
        self.terminate_instance_impl()

    def enable_auto_shutdown(self, timeout_minutes=None):
        if timeout_minutes is None:
            timeout_minutes = cloud_config.get_flag("autoshutdown_minutes")
        self.auto_shutdown_timeout_minutes = timeout_minutes
        self.run_command(
            f"(echo '{make_autoshutdown_script()}' > /tmp/autoshutdown.sh) && chmod +x /tmp/autoshutdown.sh"
        )
        self.run_command("echo 1")  # run noop to update auto_shutdown

    def disable_auto_shutdown(self):
        self.auto_shutdown_timeout_minutes = None
        self.run_command(
            "(kill -9 $(cat /tmp/autoshutdown.pid) && rm -f /tmp/autoshutdown.pid) || true"
        )

    def wait_for_ssh_ready(self, timeout=600, interval=0.5):
        def is_up():
            try:
                ip = self.public_ip()
            except Exception as e:
                return False
            if ip is not None:
                with closing(
                    socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ) as sock:
                    sock.settimeout(2)
                    conn = sock.connect_ex((ip, 22)) == 0
                    return conn
            return False

        try:
            wait_for(
                is_up,
                timeout=timeout,
                interval=interval,
                desc=f"Waiting for {self.uuid()} to be ready",
            )
        except TimeoutError:
            logger.error(
                f"Gateway {self.uuid()} is not ready after {timeout} seconds, run `skyplane deprovision` to clean up resources"
            )
            raise TimeoutError(
                f"{self.uuid()} is not ready after {timeout} seconds"
            )

    def close_server(self):
        if self._ssh_client:
            self._ssh_client.close()
            self._ssh_client = None
        for tunnel in self.ssh_tunnels.values():
            tunnel.stop()
        self.flush_command_log()

    def flush_command_log(self):
        if self.command_log_file and len(self.command_log) > 0:
            with open(self.command_log_file, "a") as f:
                for log_item in self.command_log:
                    f.write(json.dumps(log_item) + "\n")
            self.command_log = []

    def add_command_log(self, command, runtime=None, **kwargs):
        self.command_log.append(
            dict(command=command, runtime=runtime, **kwargs)
        )
        self.flush_command_log()

    def run_command(self, command) -> Tuple[str, str]:
        client = self.ssh_client
        with Timer() as t:
            if self.auto_shutdown_timeout_minutes:
                command = f"(nohup /tmp/autoshutdown.sh {self.auto_shutdown_timeout_minutes} &> /dev/null < /dev/null); {command}"
            _, stdout, stderr = client.exec_command(command)
            stdout, stderr = (
                stdout.read().decode("utf-8"),
                stderr.read().decode("utf-8"),
            )
        self.add_command_log(
            command=command, stdout=stdout, stderr=stderr, runtime=t.elapsed
        )
        # print("stdout:", stdout)
        # print("stderr:", stderr)
        return stdout, stderr

    def download_file(self, remote_path, local_path):
        """Download a file from the server"""
        sftp_client = self.get_sftp_client()
        sftp_client.get(remote_path, local_path)
        sftp_client.close()

    def upload_file(self, local_path, remote_path):
        """Upload a file to the server"""
        sftp_client = self.get_sftp_client()
        sftp_client.put(local_path, remote_path)
        sftp_client.close()

    def write_file(self, content_bytes, remote_path):
        """Write a file on the server"""
        sftp_client = self.get_sftp_client()
        with sftp_client.file(remote_path, mode="wb") as f:
            f.write(content_bytes)
        sftp_client.close()

    def copy_public_key(self, pub_key_path: Path):
        """Append public key to authorized_keys file on server."""
        pub_key_path = Path(pub_key_path)
        assert (
            pub_key_path.suffix == ".pub"
        ), f"{pub_key_path} does not have .pub extension, are you sure it is a public key?"
        pub_key = Path(pub_key_path).read_text()
        self.run_command(
            f"mkdir -p ~/.ssh && (echo '{pub_key}' >> ~/.ssh/authorized_keys) && chmod 600 ~/.ssh/authorized_keys"
        )

    def install_docker(self):
        cmd = "(command -v docker >/dev/null 2>&1 || { rm -rf get-docker.sh; curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh; }); "
        cmd += "{ sudo docker stop $(docker ps -a -q); sudo docker kill $(sudo docker ps -a -q); sudo docker rm -f $(sudo docker ps -a -q); }; "
        cmd += f"(docker --version && echo 'Success, Docker installed' || echo 'Failed to install Docker'); "
        out, err = self.run_command(cmd)
        docker_version = out.strip().split("\n")[-1]
        if not docker_version.startswith("Success"):
            raise RuntimeError(
                f"Failed to install Docker on {self.region_tag}, {self.public_ip()}: OUT {out}\nERR {err}"
            )

    def pull_docker(self, gateway_docker_image):
        docker_out, docker_err = self.run_command(
            f"sudo docker pull {gateway_docker_image}"
        )
        if (
            "Status: Downloaded newer image" not in docker_out
            and "Status: Image is up to date" not in docker_out
        ):
            raise RuntimeError(
                f"Failed to pull docker image {gateway_docker_image} on {self.region_tag}, {self.public_ip()}: OUT {docker_out}\nERR {docker_err}"
            )

    def start_gateway(
        self,
        gateway_docker_image: str,
        gateway_program_path: str,
        gateway_info_path: str,
        log_viewer_port=8888,
        use_bbr=False,
        use_compression=False,
        e2ee_key_bytes=None,
        use_socket_tls=False,
    ):
        def check_stderr(tup):
            assert tup[1].strip() == "", f"Command failed, err: {tup[1]}"

        desc_prefix = (
            f"Starting gateway {self.uuid()}, host: {self.public_ip()}"
        )

        # increase TCP connections, enable BBR optionally and raise file limits
        check_stderr(
            self.run_command(
                make_sysctl_tcp_tuning_command(cc="bbr" if use_bbr else "cubic")
            )
        )
        retry_backoff(self.install_docker, exception_class=RuntimeError)

        # start log viewer
        self.run_command(make_dozzle_command(log_viewer_port))

        # copy cloud configuration
        docker_envs = {"SKYPLANE_IS_GATEWAY": "1"}
        if config_path.exists():
            self.upload_file(config_path, f"/tmp/{config_path.name}")
            docker_envs["SKYPLANE_CONFIG"] = f"/pkg/data/{config_path.name}"

        # fix issue 312, retry boto3 credential calls to instance metadata service
        if self.provider == "aws":
            docker_envs["AWS_METADATA_SERVICE_NUM_ATTEMPTS"] = "4"
            docker_envs["AWS_METADATA_SERVICE_TIMEOUT"] = "10"

        # pull docker image and start container
        with Timer() as t:
            retry_backoff(
                partial(self.pull_docker, gateway_docker_image),
                exception_class=RuntimeError,
            )

        logger.fs.debug(f"{desc_prefix} docker pull in {t.elapsed}")
        logger.fs.debug(f"{desc_prefix}: Starting gateway container")
        docker_run_flags = f"-d --log-driver=local --log-opt max-file=16 --ipc=host --network=host --ulimit nofile={1024 * 1024}"
        docker_run_flags += " --mount type=tmpfs,dst=/skyplane,tmpfs-size=$(($(free -b  | head -n2 | tail -n1 | awk '{print $2}')/2))"
        docker_run_flags += (
            f" -v /tmp/{config_path.name}:/pkg/data/{config_path.name}"
        )

        # copy service account files
        if self.provider == "gcp":
            service_key_path = (
                compute.GCPAuthentication().get_service_account_key_path()
            )
            service_key_file = os.path.basename(service_key_path)
            self.upload_file(service_key_path, f"/tmp/{service_key_file}")
            docker_envs[
                "GCP_SERVICE_ACCOUNT_FILE"
            ] = f"/pkg/data/{service_key_file}"
            docker_run_flags += (
                f" -v /tmp/{service_key_file}:/pkg/data/{service_key_file}"
            )

        # set default region for boto3 on AWS
        if self.provider == "aws":
            docker_envs["AWS_DEFAULT_REGION"] = self.region_tag.split(":")[1]

        # copy E2EE keys
        if e2ee_key_bytes is not None:
            e2ee_key_file = "e2ee_key"
            self.write_file(e2ee_key_bytes, f"/tmp/{e2ee_key_file}")
            docker_envs["E2EE_KEY_FILE"] = f"/pkg/data/{e2ee_key_file}"
            docker_run_flags += (
                f" -v /tmp/{e2ee_key_file}:/pkg/data/{e2ee_key_file}"
            )

        # upload gateway programs and gateway info
        gateway_program_file = os.path.basename(gateway_program_path).replace(
            ":", "_"
        )
        gateway_info_file = os.path.basename(gateway_info_path).replace(
            ":", "_"
        )
        self.upload_file(
            gateway_program_path, f"/tmp/{gateway_program_file}"
        )  # upload gateway program
        self.upload_file(
            gateway_info_path, f"/tmp/{gateway_info_file}"
        )  # upload gateway info
        docker_envs["GATEWAY_PROGRAM_FILE"] = f"/pkg/data/gateway_program.json"
        docker_envs["GATEWAY_INFO_FILE"] = f"/pkg/data/gateway_info.json"
        docker_run_flags += (
            f" -v /tmp/{gateway_program_file}:/pkg/data/gateway_program.json"
        )
        docker_run_flags += (
            f" -v /tmp/{gateway_info_file}:/pkg/data/gateway_info.json"
        )
        gateway_daemon_cmd = f"/etc/init.d/stunnel4 start && python -u /pkg/skyplane/gateway/gateway_daemon.py --chunk-dir /skyplane/chunks"

        # update docker flags
        docker_run_flags += " " + " ".join(
            f"--env {k}={v}" for k, v in docker_envs.items()
        )

        gateway_daemon_cmd += f" --region {self.region_tag} {'--use-compression' if use_compression else ''}"
        gateway_daemon_cmd += (
            f" {'--disable-e2ee' if e2ee_key_bytes is None else ''}"
        )
        gateway_daemon_cmd += (
            f" {'--disable-tls' if not use_socket_tls else ''}"
        )
        escaped_gateway_daemon_cmd = gateway_daemon_cmd.replace('"', '\\"')
        docker_launch_cmd = f'sudo docker run {docker_run_flags} --name skyplane_gateway {gateway_docker_image} /bin/bash -c "{escaped_gateway_daemon_cmd}"'
        logger.fs.info(f"{desc_prefix}: {docker_launch_cmd}")
        start_out, start_err = self.run_command(docker_launch_cmd)
        logger.fs.debug(desc_prefix + f": Gateway started {start_out.strip()}")
        assert (
            not start_err.strip()
        ), f"Error starting gateway:\n{start_out.strip()}\n{start_err.strip()}"

        gateway_container_hash = start_out.strip().split("\n")[-1][:12]
        self.gateway_log_viewer_url = f"http://127.0.0.1:{self.tunnel_port(8888)}/container/{gateway_container_hash}"
        logger.fs.debug(
            f"{self.uuid()} log_viewer_url = {self.gateway_log_viewer_url}"
        )
        self.gateway_api_url = f"http://127.0.0.1:{self.tunnel_port(8080 + 1)}"
        logger.fs.debug(
            f"{self.uuid()} gateway_api_url = {self.gateway_api_url}"
        )

        # wait for gateways to start (check status API)
        http_pool = urllib3.PoolManager()

        def is_api_ready():
            try:
                api_url = f"{self.gateway_api_url}/api/v1/status"
                status_val = json.loads(
                    http_pool.request("GET", api_url).data.decode("utf-8")
                )
                is_up = status_val.get("status") == "ok"
                return is_up
            except Exception:
                return False

        try:
            logging.disable(logging.CRITICAL)
            wait_for(
                is_api_ready,
                timeout=30,
                interval=0.1,
                desc=f"Waiting for gateway {self.uuid()} to start",
            )
        except TimeoutError as e:
            logger.fs.error(f"Gateway {self.instance_name()} is not ready {e}")
            logger.fs.warning(
                desc_prefix + " gateway launch command: " + docker_launch_cmd
            )
            logs, err = self.run_command(
                f"sudo docker logs skyplane_gateway --tail=100"
            )
            logger.fs.error(f"Docker logs: {logs}\nerr: {err}")
            logger.fs.exception(e)
            raise e from None
        finally:
            logging.disable(logging.NOTSET)

    def create(
        region_tag: str,
        type: ServerType,
        instance_type: str,
        name: Optional[str] = None,
        boot_disk_size_gb: Optional[int] = 10,
        metadata: Optional[List] = [],
    ):
        if region_tag.startswith("aws:"):
            from clouds.aws.server import AWSServer

            return AWSServer(
                region_tag=region_tag,
                type=type,
                instance_name=name,
                instance_type=instance_type,
                boot_disk_size_gb=boot_disk_size_gb,
                metadata=metadata,
            )
        elif region_tag.startswith("gcp:"):
            from clouds.gcp.server import GCPServer

            return GCPServer(
                region_tag=region_tag,
                type=type,
                instance_name=name,
                instance_type=instance_type,
                boot_disk_size_gb=boot_disk_size_gb,
                metadata=metadata,
            )
        else:
            raise NotImplementedError(f"Unsupported region_tag {region_tag}")

    def start_controller(self, token=None):
        self.run_command("sudo apt -y install wireguard")
        self.run_command(
            "curl https://releases.rancher.com/install-docker/20.10.sh | sh"
        )
        stdout, stderr = self.run_command(
            f'curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--tls-san {self.public_ip()}"  sh -s - --node-external-ip={self.public_ip()} --flannel-backend=wireguard-native --flannel-external-ip'
        )
        if not token:
            token, _ = self.run_command("sudo k3s token create")
            token = token.strip()

        stdout, stderr = self.run_command("sudo less /etc/rancher/k3s/k3s.yaml")
        config_yml = stdout.strip()
        config = yaml.safe_load(config_yml)
        config["clusters"][0]["cluster"][
            "server"
        ] = f"https://{self.public_ip()}:6443"

        # TODO: change to write this to .skyatc
        with open("k3s.yaml", "w") as f:
            f.write(yaml.dump(config, default_flow_style=False))


        # pull and run autoscaling docker image 
        docker_envs = {"token": token, "cluster_ip": self.public_ip(), "PYTHONUNBUFFERED": "1", "config_path": "/pkg/data/k3s.yaml"}
        docker_run_flags = ""

        # copy cloud configuration
        config_path = __config_root__ / "config"
        self.upload_file(config_path, f"/tmp/{config_path.name}")
        docker_envs["SKYPLANE_CONFIG"] = f"/pkg/data/{config_path.name}"
        docker_run_flags += f" -v /tmp/{config_path.name}:/pkg/data/{config_path.name}"

        # copy credentials: gcp
        service_key_path = skyplane.compute.GCPAuthentication().get_service_account_key_path()
        service_key_file = os.path.basename(service_key_path)
        self.upload_file(service_key_path, f"/tmp/{service_key_file}")
        docker_envs["GCP_SERVICE_ACCOUNT_FILE"] = f"/pkg/data/{service_key_file}"
        docker_run_flags += f" -v /tmp/{service_key_file}:/pkg/data/{service_key_file}"

        # copy credentials: aws
        aws_cred = skyplane.compute.AWSAuthentication().get_boto3_session().get_credentials()
        docker_envs["AWS_ACCESS_KEY_ID"] = aws_cred.access_key
        docker_envs["AWS_SECRET_ACCESS_KEY"] = aws_cred.secret_key

        docker_run_flags += " " + " ".join(f"--env {k}={v}" for k, v in docker_envs.items())

        docker_image = "sarahwooders/skyatc-autoscaler"
        print("Pulling autoscaler container...")
        self.run_command(f"sudo docker pull {docker_image}:latest")

        # link to config file
        docker_run_flags += " -v /etc/rancher/k3s/k3s.yaml:/pkg/data/k3s.yaml"
        docker_run_cmd = f"sudo docker run -d -p 8000:8000 {docker_run_flags} --network=host sarahwooders/skyatc-autoscaler"
        print(docker_run_cmd)
        stdout, stderr = self.run_command(docker_run_cmd)
        print("DOCKER", stdout, stderr)

        # TODO: copy up cloud credentials 


        return config, token
    

    def wait_package_lock(self): 
        stdout, stderr = self.run_command(
            'while sudo fuser /var/lib/dpkg/lock >/dev/null 2>&1 \
                  || sudo fuser /var/lib/dpkg/lock-frontend >/dev/null 2>&1 \
                  || sudo fuser /var/lib/apt/lists/lock >/dev/null 2>&1; do \
                echo "Waiting for release of dpkg/apt locks..." \
                sleep 1 \
            done'
        )
        print("waiting for locks", stdout, stderr)

    def start_worker(self, public_ip, token, nvidia_drivers=True):
        # need to wait for package lock at startup time
        #self.wait_package_lock()
        while True: 
            stdout, stderr = self.run_command("sudo apt -y install wireguard wireguard-dkms")
            #print("install wiregaurd", stdout, "ERROR", stderr)
            if "Could not get lock" in stdout or "Could not get lock" in stderr: 
                time.sleep(1)
                continue 

            stdout, stderr = self.run_command(
                "sudo modprobe wireguard && lsmod | grep wireguard"
            )
            #print("wiregaurd:", stdout, stderr)
            assert "FATAL" not in stderr, "Failed to load wireguard module"
            break
 
        self.run_command(
            "curl https://releases.rancher.com/install-docker/20.10.sh | sh"
        )
        stdout, stderr = self.run_command("echo hello")
        self.run_command(
            "curl https://raw.githubusercontent.com/GoogleCloudPlatform/compute-gpu-installation/main/linux/install_gpu_driver.py --output install_gpu_driver.py"
        )

        # check and install NVIDIA drivers
        if nvidia_drivers:
            stdout, _ = self.run_command("nvidia-smi")
            if "NVIDIA_SMI" not in stdout:
                self.install_nvidia_drivers()

            # install NVIDIA container toolkit
            self.run_command(
                "curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
                && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
                  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
                  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
                && \
                  sudo apt-get update"
            )
            self.run_command("sudo apt-get install -y nvidia-container-toolkit")
            self.run_command(
                "sudo apt install -y nvidia-container-runtime cuda-drivers-fabricmanager-515 nvidia-headless-515-server"
            )
            print("Installed container runtime")

            # restart containerd
            self.run_command(
                "sudo nvidia-ctk runtime configure --runtime=containerd"
            )
            self.run_command("sudo systemctl restart containerd")
            print("Configured containerd")

        # start k3
        # TODO: use private IPs if in the same cloud as the controllers - otherwise use public IPs (enable multicloud)
        # command = f"curl -sfL https://get.k3s.io | K3S_URL=https://{public_ip}:6443 K3S_TOKEN={token} sh -"
        command = f'curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="agent --server https://{public_ip}:6443 --token {token}" sh -s - --node-external-ip={self.public_ip()}'
        print(command)
        stdout, stderr = self.run_command(command)
        print("Started K3 agent")

        ## check if NVIDIA drivers detected
        # stdout, stderr = self.run_command("sudo grep nvidia /var/lib/rancher/k3s/agent/etc/containerd/config.toml")
        # print(stdout)
        # print("errors:", stderr)

    # def start(self):
    #    if self.type = ServerType.CONTROLLER:
    #        self.start_controller()
    #    elif self.type = ServerType.WORKER:
    #        self.start_worker()
    #    else:
    #        raise ValueError("Invalid server type {self.type}")


key_root = __config_root__ / "keys"
