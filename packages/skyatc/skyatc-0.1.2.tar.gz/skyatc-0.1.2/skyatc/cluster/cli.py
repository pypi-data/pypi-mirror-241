import typer
import requests
import yaml
import subprocess
import pickle
import json
import os
from typing import Optional
from server import Server, ServerState, ServerType
from skyplane.utils.fn import do_parallel

from cluster import Cluster
from config import directory

app = typer.Typer(name="atc")


@app.command()
def create_cluster(
    num_workers: int = typer.Option(2, help="Number of workers to create."),
    controller_instance_type: str = typer.Option(
        "e2-standard-2", help="Instance type for controllers."
    ),
    worker_instance_type: str = typer.Option(
        # "g2-standard-4", help="Instance type for workers."
        "n1-standard-8",
        help="Instance type for workers.",
    ),
    region_tag: str = typer.Option(
        "gcp:us-central1-a", help="Region to create cluster in."
    ),
    cluster_name: str = typer.Option("skyatc", help="Name of cluster."),
):
    os.makedirs(directory, exist_ok=True)
    if Cluster.exists(cluster_name):
        print(f"Cluster {cluster_name} already exists.")
        cluster = Cluster.load(cluster_name)
        controller = cluster.controllers[0]
        workers = cluster.workers
    else:
        print("create cluster")
        # create controller instances
        controller = Server.create(
            region_tag=region_tag,
            type=ServerType.CONTROLLER,
            #name=f"controller",
            boot_disk_size_gb=200,
            instance_type=controller_instance_type,
        )

        # create worker instances
        workers = []
        for i in range(num_workers):
            server = Server.create(
                region_tag=region_tag,
                type=ServerType.WORKER,
                # name=f"worker-{i}",
                boot_disk_size_gb=200,
                instance_type=worker_instance_type,
            )
            workers.append(server)

        do_parallel(lambda node: node.provision(), workers + [controller], spinner=True, spinner_persist=True, desc="Provisioning instances...")

    # start controller
    config, token = controller.start_controller()
    public_ip = controller.public_ip()

    # save cluster info
    cluster = Cluster(
        workers=workers,
        controllers=[controller],
        name=cluster_name,
        cluster_ip=public_ip,
        config=config,
        token=token,
    )
    cluster.save()
    print(f"Successfully created cluster {cluster.cluster_name}.")

    # start workers
    do_parallel(lambda node: node.start_worker(public_ip, token), workers, spinner=True, spinner_persist=True, desc="Starting workers...")

    # add nvidia device plugin
    cluster.add_nvidia_device_plugin()

    # update kubectl
    kubeconfig = f"{directory}/{cluster.cluster_name}/k3s.yaml"
    os.environ["KUBECONFIG"] = kubeconfig
    # return kubeconfig
    return cluster_name

@app.command()
def update_cluster(
    cluster_name: str = typer.Option("skyatc", help="Name of cluster."),
):
    cluster = Cluster.load(cluster_name)
    controller = cluster.controllers[0]
    workers = cluster.workers

    # start controller
    config, token = controller.start_controller()
    public_ip = controller.public_ip()

    # start workers
    do_parallel(lambda node: node.start_worker(public_ip, token), workers, spinner=True, spinner_persist=True, desc="Starting workers...")

    # add nvidia device plugin
    cluster.add_nvidia_device_plugin()

    # update kubectl
    kubeconfig = f"{directory}/{cluster.cluster_name}/k3s.yaml"
    os.environ["KUBECONFIG"] = kubeconfig
    # return kubeconfig
    return cluster_name



@app.command()
def add_worker(
    cluster_name: str = typer.Option("skyatc", help="Name of cluster."),
    worker_instance_type: str = typer.Option(
        # "c5.4xlarge", help="Instance type for workers."
        "g4dn.xlarge",
        help="Instance type for workers.",
    ),
    region_tag: str = typer.Option(
        "aws:us-west-1", help="Region to create cluster in."
    ),
):
    assert Cluster.exists(
        cluster_name
    ), f"Cluster {cluster_name} does not exist."

    # update cluster
    cluster = Cluster.load(cluster_name)

    worker = Server.create(
        region_tag=region_tag,
        type=ServerType.WORKER,
        name=None,  # f"worker-21",
        boot_disk_size_gb=200,
        instance_type=worker_instance_type,
    )
    # cluster.workers.append(worker)
    # cluster.save()

    # start worker
    worker.provision()
    worker.start_worker(cluster.cluster_ip, cluster.token, nvidia_drivers=False)

    print(
        f"Successfully added worker {worker.instance_name} to cluster {cluster_name}."
    )


@app.command()
def start_autoscaler(
    cluster_name: str = typer.Option("skyatc", help="Name of cluster."),
):
    cluster = Cluster.load(cluster_name)
    cluster_ip = cluster.cluster_ip
    response = requests.get(f"http://{cluster_ip}:8000/stop")
    print(response.text)


@app.command()
def stop_autoscaler(
    cluster_name: str = typer.Option("skyatc", help="Name of cluster."),

):
    cluster = Cluster.load(cluster_name)
    cluster_ip = cluster.cluster_ip
    response = requests.get(f"http://{cluster_ip}:8000/stop")
    print(response.text)


@app.command()
def scale(
    num_workers: int = typer.Option(2, help="Number of workers to create."),
    cluster_name: str = typer.Option("skyatc", help="Name of cluster."),
):
    cluster = Cluster.load(cluster_name)
    cluster_ip = cluster.cluster_ip
    response = requests.get(f"http://{cluster_ip}:8000/scale/{num_workers}")
    print(response.text)


@app.command()
def get_events(
    cluster_name: str = typer.Option("skyatc", help="Name of cluster."),
):
    cluster = Cluster.load(cluster_name)
    cluster.get_events()


@app.command()
def stop_cluster(
    cluster_name: str = typer.Option("skyatc", help="Name of cluster."),
):
    # stop instances in the cluster
    cluster = Cluster.load(cluster_name)
    do_parallel(lambda node: node.stop(), cluster.workers + cluster.controllers)


@app.command()
def start_cluster(
    cluster_name: str = typer.Option("skyatc", help="Name of cluster."),
):
    # start instances in the cluster
    cluster = Cluster.load(cluster_name)
    do_parallel(
        lambda node: node.start(), cluster.workers + cluster.controllers
    )
    controller = cluster.controllers[0]
    workers = cluster.workers

    # start controllers / workers
    config, token = controller.start_controller(cluster.token)
    public_ip = controller.public_ip()
    do_parallel(lambda node: node.start_worker(public_ip, token), workers)

    # update cluster
    cluster.set_cluster_ip(public_ip)
    cluster.set_config(config)
    cluster.save()
    print(f"Successfully restarted cluster {cluster.cluster_name}.")

    # add nvidia device plugin
    cluster.add_nvidia_device_plugin()

    # update kubectl
    kubeconfig = f"{directory}/{cluster.cluster_name}/k3s.yaml"
    os.environ["KUBECONFIG"] = kubeconfig


@app.command()
def delete_cluster(
    cluster_name: str = typer.Option("skyatc", help="Name of cluster."),
):
    # delete instances in the cluster
    cluster = Cluster.load(cluster_name)
    do_parallel(lambda node: node.terminate_instance(), cluster.workers + cluster.controllers)

    # delete cluster directory
    os.system(f"rm -rf {directory}/{cluster_name}")
    print(f"Successfully deleted cluster {cluster.cluster_name}.")
    


if __name__ == "__main__":
    app()
