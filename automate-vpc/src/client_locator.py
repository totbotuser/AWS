import boto3


class ClientLocator:
    def __init__(self, client):
        self._client = boto3.client(client, region_name="us-east-1")

    def get_client(self):
        return self._client


class Ec2Client(ClientLocator):
    def __init__(self):
        super().__init__('ec2')
