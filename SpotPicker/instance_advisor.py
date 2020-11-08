#!/usr/bin/env python3

import requests

SPOT_ADVISOR_DATA_URL = 'https://spot-bid-advisor.s3.amazonaws.com/spot-advisor-data.json'


class SpotInstanceAdvisor:

    @classmethod
    def _get_advisor_data(cls):
        r = requests.get(SPOT_ADVISOR_DATA_URL)
        return r.json()

    def _get_instance_type_data(self, instance_type, region, instance_os):
        data = self._get_advisor_data()
        range_index = data['spot_advisor'][region][instance_os][instance_type]['r']
        interruption_rate = data['ranges'][range_index]['max']
        return interruption_rate

    def get_data(self, instance_type, region, instance_os='Linux'):
        interruption_rate = self._get_instance_type_data(instance_type, region, instance_os)
        return dict(type=instance_type, os=instance_os, region=region, value=interruption_rate)
