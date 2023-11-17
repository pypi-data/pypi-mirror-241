import time
import pytest
from typer.testing import CliRunner
from cli import app

# from cli import create_cluster, scale, delete_cluster
from cluster import Cluster, ClusterConnector

runner = CliRunner()


class TestCluster:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Setup: Create a cluster before each test method and get its name
        self.cluster_name = "test"
        result = runner.invoke(
            app,
            [
                "create-cluster",
                "--num-workers",
                1,
                "--cluster-name",
                self.cluster_name,
            ],
        )
        assert result.exit_code == 0
        print(result.stdout)
        self.conn = ClusterConnector(
            self.cluster.config_path,
            self.cluster.token,
            self.cluster.cluster_ip,
        )
        yield
        # TODO: Delete the cluster after each test method (cleanup)

    def test_get_cluster_size(self):
        cluster = Cluster(self.cluster_name)
        nodes = cluster.get_nodes()
        assert (
            len(nodes) == 2 + 1
        ), f"Invalid number of nodes in cluster {self.cluster_name}: {len(nodes)}, expected 2."

    def test_scale(self):
        from autoscaler import ClusterAutoscaler

        cluster = Cluster(self.cluster_name)
        scaler = ClusterAutoscaler(
            token=cluster.token,
            cluster_ip=cluster.cluster_ip,
            config_path=cluster.config_path,
        )
        scaler.scale(2)

    def test_pod_deploy(self):
        # deploy pods onto the cluster
        for i in range(2):
            self.conn.deploy_pod_yaml(
                "kubernetes/test_gpu.yaml", name=f"test-pod-{i}"
            )

        # wait for all pods to be RUNNING
        while True:
            pods = self.conn.list_pods()
            if all(pod.status.phase == "Running" for pod in pods):
                break
            print(pods)
            time.sleep(1)

    def test_autoscale_unscheduleable_pod(self):
        # test to make sure number of nodes gets scaled UP if pod is unschedulable
        from autoscaler import ClusterAutoscaler

        cluster = Cluster(self.cluster_name)
        scaler = ClusterAutoscaler(
            token=cluster.token,
            cluster_ip=cluster.cluster_ip,
            config_path=cluster.config_path,
        )

        # start autoscaler
        scaler.start()

        # create additional pod

        # wait for new node to be created (timeout = 5 min)

        # stop autoscaler
        scaler.stop()

    def test_autoscale_delete_node(self):
        # test to make sure new node is created if node is deleted, and pods are unschedulable
        from autoscaler import ClusterAutoscaler

        cluster = Cluster(self.cluster_name)
        scaler = ClusterAutoscaler(
            token=cluster.token,
            cluster_ip=cluster.cluster_ip,
            config_path=cluster.config_path,
        )

        # start autoscaling
        scaler.start()
