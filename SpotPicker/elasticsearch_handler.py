"""
Handles communication with Elasticsearch.
"""


from datetime import datetime

from elasticsearch import Elasticsearch

from SpotPicker.base import Base


class ElasticsearchHandler(Base):
    def __init__(self, host, port, index):
        super().__init__()
        self.client = Elasticsearch("http://{0}:{1}".format(host, port))
        self.index = index

    def push_data(self, data: dict):
        """
        Send data to Elasticsearch
        :param data: Dict with data that needs sending to Elasticsearch.
            Assumes (region, type, os, value) keys are present
        """
        body = {
            "timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "region": data['region'],
            "type": data['type'],
            "os": data['os'],
            "value": data['value']
        }
        self.client.index(index=self.index, body=body)
