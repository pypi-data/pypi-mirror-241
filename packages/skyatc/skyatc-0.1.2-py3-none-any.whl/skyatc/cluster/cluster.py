from typing import List, Optional
import urllib.parse
import urllib.parse
import os
import pickle
from uuid import uuid4
from server import Server
from config import directory
import yaml
from kubernetes import client, config, watch


class ClusterConnector:

    """Connection to K3 cluster"""

    def __init__(self, config_path, token, cluster_ip):
        self.config_path = config_path
        self.token = token
        self.cluster_ip = cluster_ip
        self._kube_client = None
        self._kube_events = None

    @property
    def kube_client(self):
        # Connect to python kube client
        if self._kube_client is None:
            config.load_kube_config(config_file=self.config_path)
            self._kube_client = client.CoreV1Api()
        return self._kube_client

    @property
    def kube_events(self):
        # Client to listen to k8 events
        if self._kube_events is None:
            config.load_kube_config(config_file=self.config_path)
            self._kube_events = watch.Watch()
        return self._kube_events

    def listen_to_events(self):
        # Stream events from all namespaces
        for event in self.kube_events.stream(
            self.kube_events.list_event_for_all_namespaces
        ):
            print(
                f"Event: {event['type']} "
                f"Object: {event['object'].kind} "
                f"Name: {event['object'].metadata.name} "
                f"Reason: {event['object'].reason} "
                f"Message: {event['object'].message}"
            )

    def list_gpu_pods(self):
        # list pods which require a GPU
        ret = self.kube_client.list_pod_for_all_namespaces(watch=False)
        gpu_pods = []
        for pod in ret.items:
            gpu_required = False
            containers = pod.spec.containers

            # Check if any container within the pod requires a GPU
            for container in containers:
                resources = container.resources
                if (
                    resources
                    and resources.limits
                    and "nvidia.com/gpu" in resources.limits
                ):
                    gpu_required = True

            if gpu_required:
                gpu_pods.append(pod)

            print(
                f"Pod Name: {pod.metadata.name}, "
                f"Namespace: {pod.metadata.namespace}, "
                f"Scheduling Status: {pod.status.phase}, "
                f"Requires GPU: {gpu_required}"
            )

    def list_nodes(self):
        # list number of nodes in cluster
        nodes = self.kube_client.list_node().items
        return nodes

    def deploy_pod_yaml(self, yaml_path, name="skyatc-pod"):
        # Read the YAML file for the pod definition
        with open(yaml_path, "r") as yaml_file:
            pod_manifest = yaml_file.read()
        pod_manifest["metadata"]["name"] = name

        # Create the pod in the cluster
        try:
            api_response = self.kube_client.create_namespaced_pod(
                body=pod_manifest,
                namespace="default",  # Set the desired namespace
            )
            print("Pod created. status='%s'" % str(api_response.status))
        except Exception as e:
            print(f"Error: {e}")

    def deploy_pod_container(self, image, name="skyatc-pod"):
        # Create the pod in the cluster
        try:
            api_response = self.kube_client.create_namespaced_pod(
                body=client.V1Pod(
                    metadata=client.V1ObjectMeta(name=name),  # Set the pod name
                    spec=client.V1PodSpec(
                        containers=[
                            client.V1Container(
                                name=name,  # Set the container name
                                image=image,  # Set the container image
                            )
                        ]
                    ),
                ),
                namespace="default",  # Set the desired namespace
            )
            print("Pod created. status='%s'" % str(api_response.status))
        except Exception as e:
            print(f"Error: {e}")

    def list_pods(self):
        # list pods in cluster
        pods = self.kube_client.list_pod_for_all_namespaces().items
        return pods


class Cluster:

    """Represention of a k3s cluster."""

    def __init__(
        self,
        controllers: List[Server],
        workers: List[Server],
        cluster_ip: Optional[str] = None,
        token: Optional[str] = None,
        config=None,
        name: Optional[str] = None,
    ):
        self.controllers = controllers
        self.workers = workers
        self.cluster_ip = cluster_ip
        self.config = config
        self.token = token
        self.cluster_name = (
            name if name is not None else "cluster-" + str(uuid4())[:8]
        )

        os.makedirs(os.path.join(directory, self.cluster_name), exist_ok=True)

        # create k3s.yaml file
        self.config_path = f"{directory}/{self.cluster_name}/k3s.yaml"
        if config:
            self.set_config(config)

    def save(self):
        path = os.path.join(directory, f"{self.cluster_name}/cluster.pkl")
        print(
            {
                "workers": self.workers,
                "controllers": self.controllers,
                "cluster_ip": self.cluster_ip,
                "token": self.token,
            }
        )
        pickle.dump(
            {
                "workers": self.workers,
                "controllers": self.controllers,
                "cluster_ip": self.cluster_ip,
                "token": self.token,
            },
            open(path, "wb"),
        )

    @property
    def public_ip(self):
        return self.controllers[0].public_ip()

    def set_cluster_ip(self, cluster_ip: str):
        self.cluster_ip = cluster_ip

    def set_token(self, token: str):
        self.token = token
        open(f"{directory}/{self.cluster_name}/token.txt", "w").write(token)

    def set_config(self, config):
        self.config = config
        with open(self.config_path, "w") as f:
            f.write(yaml.dump(self.config, default_flow_style=False))

    @staticmethod
    def exists(cluster_name: str):
        return os.path.exists(os.path.join(directory, f"{cluster_name}"))

    @staticmethod
    def load(cluster_name: str):
        path = os.path.join(directory, f"{cluster_name}")
        if not os.path.exists(path):
            raise ValueError(f"Cluster {cluster_name} does not exist.")
        data = pickle.load(open(f"{path}/cluster.pkl", "rb"))

        config = yaml.load(
            open(f"{directory}/{cluster_name}/k3s.yaml", "r"),
            Loader=yaml.FullLoader,
        )
        public_ip = urllib.parse.urlparse(
            config["clusters"][0]["cluster"]["server"]
        ).hostname

        # token = open(f"{directory}/{cluster_name}/token.txt", "r").read()

        return Cluster(
            controllers=data["controllers"],
            workers=data["workers"],
            cluster_ip=public_ip,
            token=data["token"],
            name=cluster_name,
        )

    def add_worker(self, worker: Server):
        self.workers.append(worker)

    def add_nvidia_device_plugin(self):
        stdout = os.system(
            f"kubectl --kubeconfig {directory}/{self.cluster_name}/k3s.yaml apply -f kubernetes/nvidia-device-plugin.yml"
        )
        print("Nvidia device plugin:", stdout)
