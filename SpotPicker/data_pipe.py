"""
This module sets an interface between data backends and data extraction modules.
It defines a DataQueue which is used to store all items that need sending to DataBackends
as well as a get_data function that matches instance types with Spot Instance Advisor data.
"""


import boto3
from elasticsearch.exceptions import ElasticsearchException
from influxdb.exceptions import InfluxDBClientError

from SpotPicker.base import Base
from SpotPicker.instance_advisor import SpotInstanceAdvisor
from SpotPicker.spots import SpotRequests

DataQueue = []
DataBackends = []


def get_client():
    """
    Initialize the EC2 Client
    :return: boto3.session.Session.client
    """
    return boto3.client('ec2')


def get_data():
    """
    Get all currently used instance types and add their respective Spot Instance Advisor results to the DataQueue.
    """
    client = get_client()
    for instance_type in SpotRequests(client).get_spot_instance_types():
        DataQueue.append(SpotInstanceAdvisor().get_data(instance_type, client.meta.region_name))


class DataPusher(Base):

    def push_data(self, data: dict):
        """
        Push data to all available backends.
        Available backends should be stored in DataBackends as a callable object.
        """
        for backend in DataBackends:
            try:
                backend.push_data(data)
            except (InfluxDBClientError, ElasticsearchException) as exc:
                self.logger.warning("%s: %s", type(exc), exc)

    def dequeue(self):
        """
        Push queued items.
        """
        while len(DataQueue) > 0:
            self.push_data(DataQueue.pop(0))
