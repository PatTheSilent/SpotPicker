# TODO:
#  - ProductDescription mapping to OS for Spot Instance Advisor


class SpotRequests:
    def __init__(self, client):
        self.client = client

    def _get_spot_requests(self, max_results=1000):
        return self.client.describe_spot_instance_requests(MaxResults=max_results)['SpotInstanceRequests']

    def get_spot_instance_types(self):
        instance_types = []
        for instance_request in self._get_spot_requests():
            instance_types.append(instance_request['LaunchSpecification']['InstanceType'])
        return set(instance_types)

