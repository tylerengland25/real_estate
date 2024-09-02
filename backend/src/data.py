import requests
from typing import Any, Dict, List
from configs import AWSConfig, APIConfig

class APIConnection:
    def __init__(self, api_config: APIConfig) -> None:
        self.api_config = api_config

    def fetch_data(self) -> Dict[str, Any]:
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
    def __init__(self, aws_config: AWSConfig) -> None:
        self.aws_config = aws_config
        self.client = self.aws_config.get_client()

    def write_data(self, data: List[Dict[str, Any]]) -> None:
        table_name = self.aws_config.table_name
        for item in data:
            self.client.put_item(
                TableName=table_name,
                Item={k: {'S': str(v)} for k, v in item.items()}
            )

class DataPipeline:
    def __init__(self, api_connection: APIConnection, db_connection: DBConnection) -> None:
        self.api_connection = api_connection
        self.db_connection = db_connection

    def run(self) -> None:
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