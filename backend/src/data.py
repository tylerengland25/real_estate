"""
data.py.

This module contains a class to manage the data pipeline process.

Classes:
    DataPipeline: A class to manage the data pipeline process.
"""

from connections import APIConnection, DBConnection


class DataPipeline:
    """
    Class to manage the data pipeline process.

    Attributes:
        api_connection (APIConnection): API connection instance.
        db_connection (DBConnection): Database connection instance.
    """

    def __init__(
        self, api_connection: APIConnection, db_connection: DBConnection
    ) -> None:
        """
        Initializes the DataPipeline class with the provided API and database
        connections.

        Args:
            api_connection (APIConnection): API connection instance.
            db_connection (DBConnection): Database connection instance.
        """
        self.api_connection = api_connection
        self.db_connection = db_connection

    def run(self) -> None:
        """
        Runs the data pipeline process.

        Fetches data from the API and writes it to the database.
        """
        data = self.api_connection.fetch_data()
        self.db_connection.write_data(data)
