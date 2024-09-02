import boto3
from typing import Optional, Dict, Any

class AWSConfig:
    def __init__(self, access_key: str, secret_key: str, region: str, db_name: str, table_name: str) -> None:
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region
        self.db_name = db_name
        self.table_name = table_name
        self.client = self._create_client()

    def _create_client(self) -> boto3.client:
        return boto3.client(
            'dynamodb',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region
        )

    def get_client(self) -> boto3.client:
        return self.client

class APIConfig:
    def __init__(self, base_url: str, endpoint: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None) -> None:
        self.base_url = base_url
        self.endpoint = endpoint
        self.headers = headers
        self.params = params

    def get_full_url(self) -> str:
        return f"{self.base_url}/{self.endpoint}"