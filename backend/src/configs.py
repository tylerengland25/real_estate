import boto3

class AWSConfig:
    def __init__(self, access_key, secret_key, region, db_name, table_name):
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region
        self.db_name = db_name
        self.table_name = table_name
        self.client = self._create_client()

    def _create_client(self):
        return boto3.client(
            'dynamodb',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region
        )

    def get_client(self):
        return self.client

class APIConfig:
    def __init__(self, base_url, endpoint, headers=None, params=None):
        self.base_url = base_url
        self.endpoint = endpoint
        self.headers = headers
        self.params = params

    def get_full_url(self):
        return f"{self.base_url}/{self.endpoint}"