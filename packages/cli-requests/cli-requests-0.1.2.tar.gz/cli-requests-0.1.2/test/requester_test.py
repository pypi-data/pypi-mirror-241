import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import unittest
import requests
from unittest.mock import patch, MagicMock
from cli_requests.requester import Requester
from cli_requests.exceptions import HttpRequestError, CliRequestsError


class TestRequester(unittest.TestCase):
    def setUp(self):
        self.requester = Requester()

    @patch('requests.request')
    def test_successful_request(self, mock_request):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_request.return_value = mock_response

        url = "https://example.com"
        response = self.requester.request(url)

        self.assertEqual(response, mock_response)

    @patch('requests.request')
    def test_http_error_request(self, mock_request):
        mock_response = MagicMock()
        mock_response.text = "Error Message"
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(response=mock_response)
        mock_request.return_value = mock_response

        url = "https://example.com/error_endpoint"

        with self.assertRaises(HttpRequestError) as context:
            response = self.requester.request(url, nocolor=True)

        expected_error_text = f"HTTP Error:"
        self.assertTrue(str(context.exception).startswith(expected_error_text))

    @patch('requests.request')
    def test_connection_error_request(self, mock_request):
        mock_request.side_effect = requests.exceptions.ConnectionError("Connection Error")

        url = "https://example.com"

        with self.assertRaises(CliRequestsError) as context:
            response = self.requester.request(url)

        self.assertIn("Error Connecting:", str(context.exception))
        self.assertIn("Connection Error", str(context.exception))

    @patch('requests.request')
    def test_timeout_error_request(self, mock_request):
        mock_request.side_effect = requests.exceptions.Timeout("Timeout Error")

        url = "https://example.com"

        with self.assertRaises(CliRequestsError) as context:
            response = self.requester.request(url)

        self.assertIn("Timeout Error:", str(context.exception))
        self.assertIn("Timeout Error", str(context.exception))

if __name__ == '__main__':
    unittest.main()