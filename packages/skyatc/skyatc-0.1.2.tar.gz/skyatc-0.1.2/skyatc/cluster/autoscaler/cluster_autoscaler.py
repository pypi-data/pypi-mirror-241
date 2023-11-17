# The cluster autoscaler is a FastAPI app which runs in a single pod on the controller. 
# The autoscaler can be started with /start, which starts a thread that minotors kubernetes events for pod scheduling failures
# and idle nodes (to scale down). 
import os
import uvicorn
import argparse
import time
from multiprocessing import Event #, Process, Queue
from threading import Thread
from fastapi import FastAPI
from kubernetes import client, config, watch
from skyplane.utils.fn import do_parallel

import sys
sys.path.insert(0, ".")
from server import Server, ServerState, ServerType
from cluster import ClusterConnector

# TODO: stop using local pickle and store info with k3 (so that nodes created on controller are connected)

class ClusterAutoscaler: 
    def __init__(self, token, public_ip, config_path=os.path.expanduser("~/.skyatc/skyatc/k3s.yaml")
): 
        self.app = FastAPI()
        self.exit_flag = Event()
        self.token = token
        self.public_ip = public_ip
        self.config_path = config_path
        assert os.path.exists(config_path), f"Config path {config_path} does not exist."
        self.conn = ClusterConnector(config_path, token, public_ip)
        self.monitor_thread = None

        self.register_routes()
        self.server = uvicorn.run(self.app, host="0.0.0.0", port=8000)


    def monitor_cluster(self):
        while not self.exit_flag.is_set(): 
            # very simple policy: number of nodes = number of pods trying to be scheduled 
            num_nodes = len(self.conn.list_nodes())
            num_gpu_pods = len(self.conn.list_gpu_pods())

            if num_gpu_pods > num_nodes: 
                self.scale(num_gpu_pods)
            elif num_gpu_pods < num_nodes: 
                print("Not implemented scale down")
            
            time.sleep(1)

            
    def start(self): 
        # start cluster monitoring in new thread 
        self.monitor_thread = Thread(target=self.monitor_cluster)
        self.monitor_thread.start()

    def stop(self, event):
        self.exit_flag.set()
        print("Stopping autoscaler...")
        self.monitor_thread.join()
        print("Finished stopping autoscaler.")

    def scale(self, target_cluster_size: int): 
        num_to_create = target_cluster_size - len(self.conn.list_nodes()) + 1 # assuming 1 controller
        workers = [] 

        # TODO: implement scale down

        # TODO: have some policy to determine this
        #region_tag = "gcp:us-central1-a"
        #worker_instance_type = "n1-standard-8"

        region_tag = "aws:us-west-1"
        worker_instance_type = "g4dn.xlarge"
        for i in range(num_to_create): 
            worker = Server.create(
                region_tag=region_tag,
                type=ServerType.WORKER,
                name=None, #f"worker-21",
                boot_disk_size_gb=200,
                instance_type=worker_instance_type,
            ) 
            workers.append(worker)
        # provision workers
        do_parallel(lambda node: node.provision(), workers)

        # start workers
        do_parallel(lambda node: node.start_worker(token=self.token, public_ip=self.public_ip), workers)
        return workers

    def register_routes(self): 
        @self.app.get("/start")
        def start_autoscaler():
            # assume we have access to the k3s.config file to access the cluster 
            # very simple policy: number of nodes = number of pods trying to be scheduled 
            self.start()
        
        @self.app.get("/stop/")
        def stop_autoscaler(): 
            self.stop()
        
        @self.app.get("/scale/{new_size}")
        def scale(new_size: int): 
            # scale the cluster to new_size
            # does not work unless autoscaling is stopped
            original_size = len(self.conn.list_nodes()) - 1
            self.scale(new_size)
            new_size = len(self.conn.list_nodes()) - 1
            return {"original_size": original_size, "new_size": new_size}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cluster autoscaler")
    parser.add_argument("--token", type=str, required=False, default=None, help="Kubernetes token.")
    parser.add_argument("--cluster-ip", type=str, required=False, default=None, help="IP address of cluster.")
    parser.add_argument("--config-path", type=str, required=False, default=None, help="Config path for k3s.")
    args = parser.parse_args()

    if args.token is None: 
        args.token = os.environ["token"]
    if args.cluster_ip is None: 
        args.cluster_ip = os.environ["cluster_ip"]
    if args.config_path is None: 
        args.config_path = os.environ["config_path"]

    assert args.cluster_ip is not None, f"Cluster IP must be specified."
    assert args.token is not None, f"Kubernetes token must be specified."
    assert args.config_path is not None, f"K3s config path must be specified."

    print(f"Started server for cluster {args.cluster_ip}")
    print("Priotizing AWS")

    # create autoscaler server
    autoscaler = ClusterAutoscaler(args.token, args.cluster_ip, args.config_path)
    #autoscaler.start()

