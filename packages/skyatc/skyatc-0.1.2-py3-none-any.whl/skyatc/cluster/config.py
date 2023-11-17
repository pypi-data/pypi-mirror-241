import os 

directory = os.path.expanduser("~/.skyatc")
gcp_worker_default_image = "projects/skyplane-broadcast/global/images/skyatc-image"
gcp_controller_default_image = "projects/ubuntu-os-cloud/global/images/family/ubuntu-2004-lts"
aws_worker_default_image = "ami-03fc99be9ed8f954c"
aws_controller_default_image = "ami-00a520120af320f4f"