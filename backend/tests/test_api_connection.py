import unittest
from unittest.mock import patch, Mock
from typing import Dict, Any
from configs import APIConfig
from data import APIConnection

class TestAPIConnection(unittest.TestCase):
    def setUp(self) -> None:
        self.api_config = APIConfig(
            base_url='https://api.example.com',
            endpoint='PLACEHOLDER',
            headers={'Authorization': 'Bearer test_token'},
            params={'param1': 'value1'}
        )
        self.api_connection = APIConnection(self.api_config)

    @patch('data.requests.get')
    def test_fetch_data_returns_expected_data_type(self, mock_get: Mock) -> None:
        # Mock the API response
        mock_response = Mock()
        expected_data: Dict[str, Any] = {'key': 'value'}
        mock_response.json.return_value = expected_data
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Call the method
        result = self.api_connection.fetch_data()

        # Assertions
        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_data)

if __name__ == '__main__':
    unittest.main()