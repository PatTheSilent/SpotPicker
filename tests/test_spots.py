from unittest import TestCase
from SpotPicker.spots import SpotRequests
import boto3
from botocore.stub import Stubber

DEFAULT_RESPOSES = {
    "describe_spot_instance_requests": {
        "SpotInstanceRequests": [
            {
                "CreateTime": "2020-01-01T00:00:00.000Z",
                "InstanceId": "i-xxxxxxxxxxxxxx",
                "LaunchSpecification": {
                    "SecurityGroups": [
                        {
                            "GroupName": "example-sg",
                            "GroupId": "sg-xxxxxxxxxxxxxx"
                        }
                    ],
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/xvda",
                            "Ebs": {
                                "DeleteOnTermination": True,
                                "VolumeSize": 64,
                                "VolumeType": "gp2"
                            }
                        }
                    ],
                    "IamInstanceProfile": {
                        "Arn": "arn:aws:iam::999999999999:instance-profile/example-profile",
                        "Name": "example-profile"
                    },
                    "ImageId": "ami-xxxxxxxx",
                    "InstanceType": "t2.xlarge",
                    "KeyName": "example-key",
                    "NetworkInterfaces": [
                        {
                            "DeleteOnTermination": True,
                            "DeviceIndex": 0,
                            "SubnetId": "subnet-284ef060"
                        }
                    ],
                    "Placement": {
                        "AvailabilityZone": "eu-west-1a",
                        "Tenancy": "default"
                    },
                    "Monitoring": {
                        "Enabled": False
                    }
                },
                "LaunchedAvailabilityZone": "eu-west-1a",
                "ProductDescription": "Linux/UNIX",
                "SpotInstanceRequestId": "sir-xxxxxxx",
                "SpotPrice": "0.107000",
                "State": "active",
                "Status": {
                    "Code": "fulfilled",
                    "Message": "Your spot request is fulfilled.",
                    "UpdateTime": "2020-11-08T10:20:53.000Z"
                },
                "Tags": [],
                "Type": "one-time",
                "InstanceInterruptionBehavior": "terminate"
            }
        ]
    }
}


class TestSpotRequests(TestCase):
    def test_get_spot_instance_types(self):
        client = boto3.client('ec2')
        stubber = Stubber(client)
        stubber.add_response('describe_spot_instance_requests', DEFAULT_RESPOSES['describe_spot_instance_requests'])
        stubber.activate()
        returned_instance_types = SpotRequests(client).get_spot_instance_types()
        self.assertSetEqual(returned_instance_types, set(["t2.xlarge"]))

