import warnings
import uuid
import json
from functools import lru_cache
from pathlib import Path
from typing import Optional, List

from cryptography.utils import CryptographyDeprecationWarning
from server import Server, ServerState, ServerState, ServerType, key_root
from config import gcp_worker_default_image, gcp_controller_default_image

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
    import paramiko

from skyplane import exceptions
from skyplane.compute.gcp.gcp_auth import GCPAuthentication
from skyplane.compute.gcp.gcp_key_manager import GCPKeyManager
from skyplane.utils import imports, logger
from skyplane.utils.fn import wait_for

# from skyplane.compute.server import Server, ServerState, key_root
# from skyplane.utils.fn import PathLike
print(key_root)


class GCPServer(Server):
    def __init__(
        self,
        region_tag: str,
        type: ServerState,
        instance_type: str,
        boot_disk_size_gb: int,
        instance_name: Optional[str] = None,
        metadata: Optional[List] = [],
    ):
        super().__init__(region_tag, type, instance_name)
        print("name", instance_name)
        assert (
            self.region_tag.split(":")[0] == "gcp"
        ), f"Region name doesn't match pattern gcp:<region> {self.region_tag}"
        self.gcp_region = self.region_tag.split(":")[1]
        self.instance_type = instance_type
        if self.type == ServerType.CONTROLLER:
            self.image_type = gcp_controller_default_image
        else: 
            self.image_type = gcp_worker_default_image
        #if self.instance_type.startswith(
        #    "n1"
        #):  # TODO: more generally, check for GPU instance type
        #    # g2 instances cannot use the deep learning API
        #    self.image_type = "projects/deeplearning-platform-release/global/images/family/pytorch-latest-gpu"
        #else:
        #    self.image_type = (
        #        "projects/ubuntu-os-cloud/global/images/family/ubuntu-2004-lts"
        #    )
        # self.image_type = "projects/ubuntu-os-cloud/global/images/family/ubuntu-2004-lts"
        print("Using image type", self.image_type)
        self.boot_disk_size_gb = boot_disk_size_gb
        self.spot = False
        self.auth = GCPAuthentication()
        self.key_manager = GCPKeyManager()
        self.key_name = f"skyplane-gcp-cert"
        self.metadata = metadata

        ## keys
        global key_root
        key_root = Path(key_root)
        key_root.mkdir(parents=True, exist_ok=True)
        if not self.key_manager.key_exists_local(self.key_name):
            self.key_manager.make_key_local(self.key_name)
        self.ssh_private_key = self.key_manager.get_private_key(self.key_name)
        self.ssh_public_key = self.key_manager.get_public_key(self.key_name)
        print("PRIVATE KEY", self.ssh_private_key, self.ssh_public_key)

    def __getstate__(self):
        self.close_server()
        state = self.__dict__.copy()
        del state["auth"]
        del state["key_manager"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.auth = GCPAuthentication()
        self.key_manager = GCPKeyManager()

    def uuid(self):
        return f"{self.region_tag}:{self.instance_name}"

    @lru_cache(maxsize=1)
    def get_gcp_instance(self):
        instances = self.auth.get_gcp_instances(self.gcp_region)
        if "items" in instances:
            for i in instances["items"]:
                if i["name"] == self.instance_name:
                    return i
        raise ValueError(
            f"No instance found with name {self.instance_name}, {self.gcp_region}, {instances}"
        )

    def get_instance_property(self, prop):
        instance = self.get_gcp_instance()
        if prop in instance:
            return instance[prop]
        else:
            return None

    def public_ip(self):
        """Get public IP for instance with GCP client"""
        return self.get_instance_property("networkInterfaces")[0][
            "accessConfigs"
        ][0].get("natIP")

    def private_ip(self):
        return self.get_instance_property("networkInterfaces")[0]["networkIP"]

    def region(self):
        return self.gcp_region

    def instance_state(self):
        state = self.get_instance_property("status")
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
        return mapping[state]

    def instance_name(self):
        return self.get_instance_property("name")

    def tags(self):
        """Get labels for instance."""
        return self.get_instance_property("labels") or {}

    def network_tier(self):
        interface = self.get_instance_property("networkInterfaces")[0]
        return interface["accessConfigs"][0]["networkTier"]

    def __repr__(self):
        return f"GCPServer(region_tag={self.region_tag}, instance_name={self.instance_name})"

    def terminate_instance_impl(self):
        self.auth.get_gcp_client().instances().delete(
            project=self.auth.project_id,
            zone=self.gcp_region,
            instance=self.instance_name,
        ).execute()

    def get_ssh_client_impl(
        self, uname="skyplane", ssh_key_password="skyplane"
    ):
        """Return paramiko client that connects to this instance."""
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh_client.connect(
                hostname=self.public_ip(),
                username=uname,
                pkey=paramiko.RSAKey.from_private_key_file(
                    str(self.ssh_private_key), password=ssh_key_password
                ),
                look_for_keys=False,
                banner_timeout=200,
            )
            return ssh_client
        except paramiko.AuthenticationException as e:
            print(e)
            raise exceptions.BadConfigException(
                f"Failed to connect to GCP server {self.uuid()}. Delete local GCP keys and retry: `rm -rf {key_root / 'gcp'}`"
            ) from e

    def get_sftp_client(self, uname="skyplane", ssh_key_password="skyplane"):
        t = paramiko.Transport((self.public_ip(), 22))
        pkey = paramiko.RSAKey.from_private_key_file(
            str(self.ssh_private_key), password=ssh_key_password
        )
        t.connect(username=uname, pkey=pkey)
        return paramiko.SFTPClient.from_transport(t)

    def open_ssh_tunnel_impl(
        self, remote_port, uname="skyplane", ssh_key_password="skyplane"
    ):
        import sshtunnel

        return sshtunnel.SSHTunnelForwarder(
            (self.public_ip(), 22),
            ssh_username=uname,
            ssh_pkey=str(self.ssh_private_key),
            ssh_private_key_password=ssh_key_password,
            host_pkey_directories=[],
            local_bind_address=("127.0.0.1", 0),
            remote_bind_address=("127.0.0.1", remote_port),
        )

    def get_ssh_cmd(self, uname="skyplane", ssh_key_password="skyplane"):
        # todo can we include the key password inline?
        return f"ssh -i {self.ssh_private_key} -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no {uname}@{self.public_ip()}"

    @imports.inject("googleapiclient.errors", pip_extra="gcp")
    def stop(errors, self):
        compute = self.auth.get_gcp_client()
        try:
            result = (
                compute.instances()
                .stop(
                    project=self.auth.project_id,
                    zone=self.gcp_region,
                    instance=self.instance_name,
                )
                .execute()
            )
            self.auth.wait_for_operation_to_complete(
                self.gcp_region, result["name"]
            )
        except Exception as e:
            print(f"Error deprovisioning {self.instance_name}")
            return False
        return True

    @imports.inject("googleapiclient.errors", pip_extra="gcp")
    def start(errors, self):
        compute = self.auth.get_gcp_client()
        try:
            result = (
                compute.instances()
                .start(
                    project=self.auth.project_id,
                    zone=self.gcp_region,
                    instance=self.instance_name,
                )
                .execute()
            )
            self.auth.wait_for_operation_to_complete(
                self.gcp_region, result["name"]
            )
        except Exception as e:
            print(f"Error starting {self.instance_name}")
            return False
        return True

    @imports.inject("googleapiclient.errors", pip_extra="gcp")
    def provision(
        errors,
        self,
        tags={"skyplane": "true"},
        gcp_premium_network=False,
        gcp_vm_uname="skyplane",
    ):
        assert self.region_tag.startswith(
            "gcp:"
        ), f"Region {self.region_tag} should be GCP region"
        compute = self.auth.get_gcp_client()
        print("INSTANCE TYPE", self.instance_type)

        req_body = {
            "name": self.instance_name,
            "machineType": f"zones/{self.gcp_region}/machineTypes/{self.instance_type}",
            "labels": tags,
            "disks": [
                {
                    "boot": True,
                    "autoDelete": True,
                    "initializeParams": {
                        "sourceImage": self.image_type,
                        "diskType": f"zones/{self.gcp_region}/diskTypes/pd-standard",
                        "diskSizeGb": self.boot_disk_size_gb,
                    },
                }
            ],
            "networkInterfaces": [
                {
                    "network": "global/networks/skyplane",
                    "accessConfigs": [
                        {
                            "name": "External NAT",
                            "type": "ONE_TO_ONE_NAT",
                            "networkTier": "PREMIUM"
                            if gcp_premium_network
                            else "STANDARD",
                        }
                    ],
                }
            ],
            "serviceAccounts": [
                {
                    "email": "default",
                    "scopes": [
                        "https://www.googleapis.com/auth/cloud-platform"
                    ],
                }
            ],
            "metadata": {
                "items": [
                    {"key": "enable-oslogin", "value": "false"},
                    {
                        "key": "ssh-keys",
                        "value": f"{gcp_vm_uname}:{self.key_manager.get_public_key(self.key_name).read_text()}\n",
                    },
                ]
                + self.metadata
            },
            "deletionProtection": False,
        }
        if self.instance_type.startswith("g") or self.instance_type.startswith(
            "n1"
        ):  # TODO: more generally, check for GPU instance type
            req_body["scheduling"] = {
                "onHostMaintenance": "TERMINATE",
                "automaticRestart": False,
            }
            req_body["metadata"]["items"].append(
                {"key": "install-nvidia-driver", "value": "true"}
            )
            #req_body["metadata"]["items"].append(
            #    {"key": "startup-script", "value": "sudo ufw allow 22"}
            #)

            # TODO: make this configurable
            gpu_type = "nvidia-tesla-t4"
            req_body["guestAccelerators"] = [
                {
                    "acceleratorCount": 1,
                    "acceleratorType": f"projects/{self.auth.project_id}/zones/{self.gcp_region}/acceleratorTypes/{gpu_type}",
                }
            ]

        # use preemtible instances if use_spot_instances is True
        if self.spot:
            req_body["scheduling"]["preemptible"] = True

        zone = self.gcp_region
        while True:
            # iteratively try to find region to provision instance in
            try:
                result = (
                    compute.instances()
                    .insert(
                        project=self.auth.project_id, zone=zone, body=req_body
                    )
                    .execute()
                )
                print("PROVISION RESULT", result)
                self.auth.wait_for_operation_to_complete(
                    self.gcp_region, result["name"]
                )

                # wait for server to reach RUNNING state
                try:
                    wait_for(
                        lambda: self.instance_state() == ServerState.RUNNING,
                        timeout=120,
                        interval=0.1,
                        desc=f"Wait for RUNNING status on {self.instance_name}",
                    )
                    self.wait_for_ssh_ready()
                except:
                    logger.fs.error(
                        f"Instance {self.instance_name} did not reach RUNNING status"
                    )
                    print(
                        f"Instance {self.instance_name} did not reach RUNNING status"
                    )
                    self.terminate_instance()
                    raise
                # self.run_command("sudo /sbin/iptables -A INPUT -j ACCEPT") # TODO: fix SSH access
                print("FINISHED PROVISIONING")
                # TODO: update server state
                break
            except errors.HttpError as e:
                # logger.fs.info(f"Exception, ensuring instance is deprovisioned: {e}")
                # print(f"Exception, ensuring instance is deprovisioned: {e}")
                # op = compute.instances().delete(project=self.auth.project_id, zone=self.gcp_region, instance=self.instance_name).execute()
                # self.auth.wait_for_operation_to_complete(self.gcp_region, op["name"])
                print("error", e.content)
                available_regions = self.check_error_available_regions(
                    e.content
                )
                if len(available_regions) == 0:
                    if e.resp.status == 409:
                        if "ZONE_RESOURCE_POOL_EXHAUSTED" in e.content:
                            raise exceptions.InsufficientVCPUException(
                                f"Got ZONE_RESOURCE_POOL_EXHAUSTED in region {self.gcp_region}"
                            ) from e
                        elif "RESOURCE_EXHAUSTED" in e.content:
                            raise exceptions.InsufficientVCPUException(
                                f"Got RESOURCE_EXHAUSTED in region {self.gcp_region}"
                            ) from e
                        elif "QUOTA_EXCEEDED" in e.content:
                            raise exceptions.InsufficientVCPUException(
                                f"Got QUOTA_EXCEEDED in region {self.gcp_region}"
                            ) from e
                        elif "QUOTA_LIMIT" in e.content:
                            raise exceptions.InsufficientVCPUException(
                                f"Got QUOTA_LIMIT in region {self.gcp_region}"
                            ) from e
                    raise
                else:
                    print(
                        f"Zone {zone}not available, trying again in {available_regions[0]}"
                    )
                    zone = available_regions[0]
            except KeyboardInterrupt:
                logger.fs.info(f"Keyboard interrupt, deleting instance {name}")
                op = (
                    compute.instances()
                    .delete(
                        project=self.auth.project_id,
                        zone=self.gcp_region,
                        instance=name,
                    )
                    .execute()
                )
                self.auth.wait_for_operation_to_complete(
                    self.gcp_region, op["name"]
                )
                raise

    def check_error_available_regions(self, error_string):
        # Parse the JSON
        data = json.loads(error_string)

        # Check if the necessary keys exist and then access the "zonesAvailable" value
        if "errors" in data and isinstance(data["errors"], list):
            for error in data["errors"]:
                if "errorInfo" in error and "metadatas" in error["errorInfo"]:
                    metadatas = error["errorInfo"]["metadatas"]
                    if "zonesAvailable" in metadatas:
                        zones_available = metadatas["zonesAvailable"]
                        print("zonesAvailable:", zones_available)
                        return zones_available.split(",")
        return []

    def install_nvidia_drivers(self):
        # GCP specific script to install NVIDIA drivers
        self.run_command(
            "curl https://raw.githubusercontent.com/GoogleCloudPlatform/compute-gpu-installation/main/linux/install_gpu_driver.py --output install_gpu_driver.py"
        )

        # server gets restarted during installation of NVIDIA drivers
        # this is a messy solution where I restart the SSH connection until NVIDIA-SMI is available
        while True:
            try:
                nvidia_stdout, nvidia_stderr = self.run_command("nvidia-smi")
                if "NVIDIA-SMI" in nvidia_stdout:
                    # NOTE: sometimes install_gpu_driver.py still needs to be run one more time (on L4 instances)
                    print("Successfully installed drivers")
                    return

                stdout, stderr = self.run_command(
                    "sudo python3 install_gpu_driver.py"
                )
                print("NVIDIA", nvidia_stdout, stdout)
            except Exception as e:
                print(e)
                self.close_server()  # restart ssh connection
                print("closed server")
