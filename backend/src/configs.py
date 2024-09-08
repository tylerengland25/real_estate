"""
configs.py

This module contains configuration classes and functions for setting up AWS services.

Classes:
    AWSConfig: A configuration class for AWS settings, including access keys, region, and DynamoDB client.
    APIConfig: A configuration class for API settings, including base URL, endpoint, headers, and parameters.
"""

from typing import Optional, Dict, Any
import boto3


class AWSConfig:
    """
    Configuration class for AWS settings.

    Attributes:
        config (Dict[str, Any]): Configuration dictionary containing AWS settings.
        client (boto3.client): Boto3 client for DynamoDB.
    """

    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Initializes the AWSConfig class with the provided configuration dictionary.

        Args:
            config (Dict[str, Any]): Configuration dictionary containing AWS settings.
        """
        self._config = config
        self.client = self._creat_client()

    def _creat_client(self) -> boto3.client:
        """
        Creates and returns a Boto3 client for DynamoDB.

        Returns:
            boto3.client: Boto3 client for DynamoDB.
        """
        return boto3.client(
            "dynamodb",
            aws_access_key_id=self._config["access_key"],
            aws_secret_access_key=self._config["secret_key"],
            region_name=self._config["region"],
        )

    def get_client(self) -> boto3.client:
        """
        Returns the Boto3 client for DynamoDB.

        Returns:
            boto3.client: Boto3 client for DynamoDB.
        """
        return self.client

    def update_config(self, config: Dict[str, Any]) -> None:
        """
        Updates the configuration dictionary with the provided configuration dictionary.

        Args:
            config (Dict[str, Any]): Configuration dictionary containing AWS settings.
        """
        self._config.update(config)


class APIConfig:
    """
    Configuration class for API settings.

    Attributes:
        config (Dict[str, Any]): Configuration dictionary containing API settings.
    """

    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Initializes the APIConfig class with the provided configuration dictionary.

        Args:
            config (Dict[str, Any]): Configuration dictionary containing API settings.
                Expects the following keys:
                    - base_url (str): Base URL for the API.
                    - endpoint (str): Endpoint for the API.
                    - headers (Dict[str, str]): Headers for the API request.
                    - params (Dict[str, str]): Parameters for the API request.
        """
        self._config = config

    def get_full_url(self) -> str:
        """
        Constructs and returns the full URL for the API request.

        Returns:
            str: Full URL for the API request.
        """
        return f"{self._config['base_url']}/{self._config['endpoint']}"

    def get_headers(self) -> Dict[str, str]:
        """
        Returns the headers for the API request.

        Returns:
            Dict[str, str]: Headers for the API request.
        """
        return self._config["headers"]

    def get_params(self) -> Dict[str, str]:
        """
        Returns the parameters for the API request.

        Returns:
            Dict[str, str]: Parameters for the API request.
        """
        return self._config["params"]
