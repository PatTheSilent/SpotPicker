"""
Handles communication with InfluxDB.
"""

from influxdb import InfluxDBClient

from datetime import datetime

from SpotPicker.base import Base


class InfluxDBHandler(Base):
    def __init__(self, host, port, user, password, db):
        """

        :param host: InfluxDB host
        :param port: InfluxDB host
        :param user: InfluxDB user
        :param password: InfluxDB password
        :param db: InfluxDB database name. Assumes a database is pre-created.
        """
        super().__init__()
        self.client = InfluxDBClient(host, port, user, password, db)

    def push_data(self, data: dict):
        """
        Send data to InfluxDB
        :param data: Dict with data that needs sending to InfluxDB. Assumes (region, type, os, value) keys are present
        """
        body = [
            {
                "measurement": "interruption_frequency",
                "tags": {
                    "region": str(data['region']),
                    "type": str(data['type']),
                    "os": str(data['os'])
                },
                "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                "fields": {
                    "value": int(data['value'])
                }
            }
        ]
        self.client.write_points(body)
