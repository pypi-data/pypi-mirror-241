import uuid
import time
import logging
import warnings

from cryptography.utils import CryptographyDeprecationWarning
from typing import Dict, Optional, List

from skyplane.compute.aws.aws_key_manager import AWSKeyManager

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
    import paramiko

from server import Server, ServerState, ServerState, ServerType, key_root
from config import aws_worker_default_image, aws_controller_default_image

from skyplane import exceptions
from skyplane.compute.aws.aws_auth import AWSAuthentication
from skyplane.utils import imports, logger
from skyplane.utils.cache import ignore_lru_cache
from skyplane.utils.fn import wait_for

from multiprocessing import BoundedSemaphore


class AWSServer(Server):
    """AWS Server class to support basic SSH operations"""

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
        assert self.region_tag.split(":")[0] == "aws"
        self.instance_id = None  # self.instance_name
        self.instance_type = instance_type
        self.boot_disk_size_gb = boot_disk_size_gb
        self.metadata = metadata
        self.auth = AWSAuthentication()
        self.aws_region = self.region_tag.split(":")[1]
        self.use_spot = False  # TODO: make configurable

        # create keys
        self.key_prefix = "skyplane"
        self.key_manager = AWSKeyManager(self.auth)
        # self.key_manager.make_key(self.aws_region, f"{self.key_prefix}-{self.aws_region}")
        self.key_manager.ensure_key_exists(
            self.aws_region, f"{self.key_prefix}-{self.aws_region}"
        )

        # set default image used for provisioning instances in AWS
        # self.image = "resolve:ssm:/aws/service/canonical/ubuntu/server/20.04/stable/current/amd64/hvm/ebs-gp2/ami-id"

        #self.image = "ami-00a520120af320f4f"  # NOTE:  hard coded for region
        if self.type == ServerType.CONTROLLER:
            self.image = aws_controller_default_image
        else: 
            self.image = aws_worker_default_image

        # TODO: fix this - not actually doing anything since not shared across processes provisioning
        self.provisioning_semaphore = BoundedSemaphore(16)

    # @functools.lru_cache(maxsize=None)
    @property
    def login_name(self) -> str:
        # update the login name according to AMI
        ec2 = self.auth.get_boto3_resource("ec2", self.aws_region)
        ec2client = ec2.meta.client
        image_info = ec2client.describe_images(
            ImageIds=[ec2.Instance(self.instance_id).image_id]
        )
        # if [r["Name"] for r in image_info["Images"]][0].split("/")[0] == "ubuntu":
        #    return "ubuntu"
        # else:
        #    return "ec2-user"
        return "ubuntu"  # TODO: fix this to be more general

    @property
    @imports.inject("boto3", pip_extra="aws")
    def boto3_session(boto3, self):
        if not hasattr(self, "_boto3_session"):
            self._boto3_session = self._boto3_session = boto3.Session(
                region_name=self.aws_region
            )
        return self._boto3_session

    def uuid(self):
        return f"{self.region_tag}:{self.instance_id}"

    def get_boto3_instance_resource(self):
        ec2 = self.auth.get_boto3_resource("ec2", self.aws_region)
        return ec2.Instance(self.instance_id)

    @ignore_lru_cache()
    def public_ip(self) -> str:
        # todo maybe eventually support VPC peering?
        return self.get_boto3_instance_resource().public_ip_address

    @ignore_lru_cache()
    def private_ip(self) -> str:
        return self.get_boto3_instance_resource().private_ip_address

    @ignore_lru_cache()
    def instance_class(self) -> str:
        return self.get_boto3_instance_resource().instance_type

    @ignore_lru_cache(ignored_value={})
    def tags(self) -> Dict[str, str]:
        tags = self.get_boto3_instance_resource().tags
        return {tag["Key"]: tag["Value"] for tag in tags} if tags else {}

    @ignore_lru_cache()
    def instance_name(self) -> Optional[str]:
        return self.tags().get("Name", None)

    def network_tier(self):
        return "PREMIUM"

    def region(self):
        return self.aws_region

    def instance_state(self):
        return ServerState.from_aws_state(
            self.get_boto3_instance_resource().state["Name"]
        )

    @property
    @ignore_lru_cache()
    def local_keyfile(self):
        key_name = self.get_boto3_instance_resource().key_name
        print("KEY NAME", key_name)
        if self.key_manager.key_exists_local(key_name):
            print("KEY FILE", self.key_manager.get_key(key_name))
            return self.key_manager.get_key(key_name)
        else:
            raise exceptions.BadConfigException(
                f"Failed to connect to AWS server {self.uuid()}. Delete local AWS keys and retry: `rm -rf {key_root / 'aws'}`"
            )

    def __repr__(self):
        return f"AWSServer(region_tag={self.region_tag}, instance_id={self.instance_id})"

    def terminate_instance_impl(self):
        iam = self.auth.get_boto3_resource("iam")

        # get instance profile name that is associated with this instance
        profile = self.get_boto3_instance_resource().iam_instance_profile
        if profile:
            profile = iam.InstanceProfile(profile["Arn"].split("/")[-1])

            # remove all roles from instance profile
            try:
                for role in profile.roles:
                    profile.remove_role(RoleName=role.name)
                # delete instance profile
                profile.delete()
            except Exception as e:
                logger.warning(
                    f"Failed to remove instance profile {profile.name}"
                )
                logger.exception(e)

        # delete instance
        self.get_boto3_instance_resource().terminate()

    def get_ssh_client_impl(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(
                self.public_ip(),
                # username="ec2-user",
                username=self.login_name,
                # todo generate keys with password "skyplane"
                pkey=paramiko.RSAKey.from_private_key_file(
                    str(self.local_keyfile)
                ),
                look_for_keys=False,
                allow_agent=False,
                banner_timeout=200,
            )
            return client
        except paramiko.AuthenticationException as e:
            raise exceptions.BadConfigException(
                f"Failed to connect to AWS server {self.uuid()}. Delete local AWS keys and retry: `rm -rf {key_root / 'aws'}`"
            ) from e

    def get_sftp_client(self):
        t = paramiko.Transport((self.public_ip(), 22))
        # t.connect(username="ec2-user", pkey=paramiko.RSAKey.from_private_key_file(str(self.local_keyfile)))
        t.connect(
            username=self.login_name,
            pkey=paramiko.RSAKey.from_private_key_file(str(self.local_keyfile)),
        )
        return paramiko.SFTPClient.from_transport(t)

    def open_ssh_tunnel_impl(self, remote_port):
        import sshtunnel

        sshtunnel.DEFAULT_LOGLEVEL = logging.FATAL
        return sshtunnel.SSHTunnelForwarder(
            (self.public_ip(), 22),
            # ssh_username="ec2-user",
            ssh_username=self.login_name,
            ssh_pkey=str(self.local_keyfile),
            host_pkey_directories=[],
            local_bind_address=("127.0.0.1", 0),
            remote_bind_address=("127.0.0.1", remote_port),
        )

    def get_ssh_cmd(self):
        # return f"ssh -i {self.local_keyfile} ec2-user@{self.public_ip()}"
        return (
            f"ssh -i {self.local_keyfile} {self.login_name}@{self.public_ip()}"
        )

    @imports.inject("botocore.exceptions", pip_extra="aws")
    def provision(
        exceptions,
        self,
        tags={"skyplane": "true"},
        aws_iam_name: str = "skyplane_gateway",
    ):
        assert self.region_tag.startswith(
            "aws:"
        ), f"Region should be AWS region {self.region_tag}"
        iam_instance_profile_name = f"{self.instance_name}_profile"
        self.key_prefix = "skyplane"

        with self.provisioning_semaphore:
            iam = self.auth.get_boto3_client("iam", self.aws_region)
            ec2 = self.auth.get_boto3_resource("ec2", self.aws_region)
            ec2_client = self.auth.get_boto3_client("ec2", self.aws_region)
            # vpcs = self.network.get_vpcs(self.aws_region)
            # assert vpcs, "No VPC found"
            # vpc = vpcs[0]

            # get subnet list
            def instance_class_supported(az):
                # describe_instance_type_offerings
                offerings_list = ec2_client.describe_instance_type_offerings(
                    LocationType="availability-zone",
                    Filters=[{"Name": "location", "Values": [az]}],
                )
                offerings = [
                    o
                    for o in offerings_list["InstanceTypeOfferings"]
                    if o["InstanceType"] == self.instance_type
                ]
                return len(offerings) > 0

            # subnets = [subnet for subnet in vpc.subnets.all() if instance_class_supported(subnet.availability_zone)]
            # assert len(subnets) > 0, "No subnets found that support specified instance class"

            def check_iam_role():
                try:
                    iam.get_role(RoleName=aws_iam_name)
                    return True
                except iam.exceptions.NoSuchEntityException:
                    return False

            def check_instance_profile():
                try:
                    iam.get_instance_profile(
                        InstanceProfileName=iam_instance_profile_name
                    )
                    return True
                except iam.exceptions.NoSuchEntityException:
                    return False

            # wait for iam_role to be created and create instance profile
            wait_for(check_iam_role, timeout=60, interval=0.5)
            iam.create_instance_profile(
                InstanceProfileName=iam_instance_profile_name,
                Tags=[{"Key": "skyplane", "Value": "true"}],
            )
            iam.add_role_to_instance_profile(
                InstanceProfileName=iam_instance_profile_name,
                RoleName=aws_iam_name,
            )
            wait_for(check_instance_profile, timeout=60, interval=0.5)

            print("KEY NAME", f"{self.key_prefix}-{self.aws_region}")

            # def start_instance(subnet_id: str):
            def start_instance():
                if self.use_spot:
                    market_options = {"MarketType": "spot"}
                else:
                    market_options = {}
                return ec2.create_instances(
                    ImageId=self.image,
                    InstanceType=self.instance_type,
                    MinCount=1,
                    MaxCount=1,
                    KeyName=f"{self.key_prefix}-{self.aws_region}",
                    TagSpecifications=[
                        {
                            "ResourceType": "instance",
                            "Tags": [
                                {"Key": "Name", "Value": self.instance_name}
                            ]
                            + [{"Key": k, "Value": v} for k, v in tags.items()],
                        }
                    ],
                    BlockDeviceMappings=[
                        {
                            "DeviceName": "/dev/sda1",
                            "Ebs": {
                                "DeleteOnTermination": True,
                                "VolumeSize": self.boot_disk_size_gb,
                                "VolumeType": "gp2",
                            },
                        }
                    ],
                    NetworkInterfaces=[
                        {
                            "DeviceIndex": 0,
                            # "Groups": [self.network.get_security_group(self.aws_region).group_id],
                            # "SubnetId": subnet_id,
                            "AssociatePublicIpAddress": True,
                            "DeleteOnTermination": True,
                        }
                    ],
                    IamInstanceProfile={"Name": iam_instance_profile_name},
                    InstanceInitiatedShutdownBehavior="terminate",
                    InstanceMarketOptions=market_options,
                )

            backoff = 1
            max_retries = 8
            max_backoff = 8
            current_subnet_id = 0
            for i in range(max_retries):
                try:
                    # instance = start_instance(subnets[current_subnet_id].id)
                    instance = start_instance()
                    break
                except exceptions.ClientError as e:
                    if i == max_retries - 1:
                        raise
                    elif "VcpuLimitExceeded" in str(e):
                        raise skyplane_exceptions.InsufficientVCPUException() from e
                    elif "Invalid IAM Instance Profile name" in str(e):
                        # TODO: suppress this
                        logger.fs.info(str(e))
                    elif "InsufficientInstanceCapacity" in str(e):
                        # try another subnet
                        current_subnet_id = (current_subnet_id + 1) % len(
                            subnets
                        )
                    else:
                        raise ValueError(
                            f"Unexpected provisioning error: {str(e)}"
                        )
                    time.sleep(backoff)
                    backoff = min(backoff * 2, max_backoff)

            assert (
                len(instance) == 1
            ), f"Expected 1 instance, got {len(instance)}"
            try:
                instance[0].wait_until_running()
                print("instance id", instance[0].id)
                self.instance_id = instance[0].id
                print("Waiting for ssh...")
                self.wait_for_ssh_ready()
            except KeyboardInterrupt:
                logger.fs.warning(
                    f"Terminating instance {instance[0].id} due to keyboard interrupt"
                )
                instance[0].terminate()
                raise
