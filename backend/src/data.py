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
        Initializes the APIConnection class with the provided API configuration.

        Args:
            api_config (APIConfig): Configuration for the API.
        """
        self.api_config = api_config

    def fetch_data(self) -> Dict[str, Any]:
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
            params=self.api_config.params
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

    def write_data(self, data: List[Dict[str, Any]]) -> None:
        """
        Writes data to the DynamoDB table.

        Args:
            data (List[Dict[str, Any]]): Data to be written to the table.
        """
        table_name = self.aws_config.table_name
        for item in data:
            self.client.put_item(
                TableName=table_name,
                Item={k: {'S': str(v)} for k, v in item.items()}
            )

class DataPipeline:
    """
    Class to manage the data pipeline process.

    Attributes:
        api_connection (APIConnection): API connection instance.
        db_connection (DBConnection): Database connection instance.
    """

    def __init__(self, api_connection: APIConnection, db_connection: DBConnection) -> None:
        """
        Initializes the DataPipeline class with the provided API and database connections.

        Args:
            api_connection (APIConnection): API connection instance.
            db_connection (DBConnection): Database connection instance.
        """
        self.api_connection = api_connection
        self.db_connection = db_connection

    def run(self) -> None:
        """
        Runs the data pipeline process: fetches data from the API and writes it to the database.
        """
        data = self.api_connection.fetch_data()
        self.db_connection.write_data(data)

# Example usage
if __name__ == "__main__":
    aws_config = AWSConfig(
        access_key='your_access_key',
        secret_key='your_secret_key',
        region='your_region',
        db_name='your_db_name',
        table_name='your_table_name'
    )

    api_config = APIConfig(
        base_url='https://api.example.com',
        endpoint='data',
        headers={'Authorization': 'Bearer your_token'},
        params={'param1': 'value1'}
    )

    api_connection = APIConnection(api_config)
    db_connection = DBConnection(aws_config)
    pipeline = DataPipeline(api_connection, db_connection)
    pipeline.run()