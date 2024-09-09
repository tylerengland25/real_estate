"""
connections.py.

This module contains functions for setting up API connections.

Classes:
    APIConnection: A class to handle API connections and data fetching.
    DBConnection: A class to handle database connections and data operations.
"""

import requests
from typing import Any, Dict, List
from configs import AWSConfig, APIConfig


class APIConnection:
    """
    Class to handle API connections and data fetching.

    Attributes:
        api_config (APIConfig): Configuration for the API.
    """

    def __init__(self, api_config: APIConfig) -> None:
        """
        Initializes the APIConnection class with the provided API
        configuration.

        Args:
            api_config (APIConfig): Configuration for the API.
        """
        self.api_config = api_config

    def get(self) -> Dict[str, Any]:
        """
        Fetches data from the API.

        Returns:
            Dict[str, Any]: Data fetched from the API.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(
            self.api_config.get_full_url(),
            headers=self.api_config.headers,
            params=self.api_config.params,
        )
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()


class DBConnection:
    """
    Class to handle database connections and data operations.

    Attributes:
        aws_config (AWSConfig): Configuration for AWS.
        client (boto3.client): Boto3 client for DynamoDB.
    """

    def __init__(self, aws_config: AWSConfig) -> None:
        """
        Initializes the DBConnection class with the provided AWS configuration.

        Args:
            aws_config (AWSConfig): Configuration for AWS.
        """
        self.aws_config = aws_config
        self.client = self.aws_config.get_client()

    def write(self, data: List[Dict[str, Any]]) -> None:
        """
        Writes data to the DynamoDB table.

        Args:
            data (List[Dict[str, Any]]): Data to be written to the table.
        """
        table_name = self.aws_config.table_name
        for item in data:
            self.client.put_item(
                TableName=table_name,
                Item={k: {"S": str(v)} for k, v in item.items()},
            )
