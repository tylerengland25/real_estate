import boto3
from typing import Optional, Dict, Any

class AWSConfig:
    """
    Configuration class for AWS settings.

    Attributes:
        access_key (str): AWS access key.
        secret_key (str): AWS secret key.
        region (str): AWS region.
        db_name (str): Name of the database.
        table_name (str): Name of the table.
        client (boto3.client): Boto3 client for DynamoDB.
    """

    def __init__(self, access_key: str, secret_key: str, region: str, db_name: str, table_name: str) -> None:
        """
        Initializes the AWSConfig class with the provided parameters.

        Args:
            access_key (str): AWS access key.
            secret_key (str): AWS secret key.
            region (str): AWS region.
            db_name (str): Name of the database.
            table_name (str): Name of the table.
        """
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region
        self.db_name = db_name
        self.table_name = table_name
        self.client = self._create_client()

    def _create_client(self) -> boto3.client:
        """
        Creates a Boto3 client for DynamoDB.

        Returns:
            boto3.client: Boto3 client for DynamoDB.
        """
        return boto3.client(
            'dynamodb',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region
        )

    def get_client(self) -> boto3.client:
        """
        Returns the Boto3 client for DynamoDB.

        Returns:
            boto3.client: Boto3 client for DynamoDB.
        """
        return self.client

class APIConfig:
    """
    Configuration class for API settings.

    Attributes:
        base_url (str): Base URL of the API.
        endpoint (str): API endpoint.
        headers (Optional[Dict[str, str]]): Headers for the API request.
        params (Optional[Dict[str, Any]]): Parameters for the API request.
    """

    def __init__(self, base_url: str, endpoint: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None) -> None:
        """
        Initializes the APIConfig class with the provided parameters.

        Args:
            base_url (str): Base URL of the API.
            endpoint (str): API endpoint.
            headers (Optional[Dict[str, str]]): Headers for the API request.
            params (Optional[Dict[str, Any]]): Parameters for the API request.
        """
        self.base_url = base_url
        self.endpoint = endpoint
        self.headers = headers
        self.params = params

    def get_full_url(self) -> str:
        """
        Constructs and returns the full URL for the API request.

        Returns:
            str: Full URL for the API request.
        """
        return f"{self.base_url}/{self.endpoint}"