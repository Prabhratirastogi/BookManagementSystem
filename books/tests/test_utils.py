from django.test import TestCase
from unittest.mock import patch
from books.utils import fetch_books_data
import requests

class UtilsTest(TestCase):

    @patch('books.utils.requests.get')
    def test_fetch_books_data_success(self, mock_get):
        # Mocking the API response
        mock_response = {
            'items': [
                {'volumeInfo': {'title': 'Test Book'}}
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        query = 'test'
        result = fetch_books_data(query)
        self.assertIsNotNone(result)
        self.assertIn('items', result)
        self.assertEqual(result['items'][0]['volumeInfo']['title'], 'Test Book')

    @patch('books.utils.requests.get')
    def test_fetch_books_data_http_error(self, mock_get):
        # Mocking an HTTP error
        mock_get.side_effect = requests.HTTPError('HTTP error')

        query = 'test'
        result = fetch_books_data(query)
        self.assertIsNone(result)

    @patch('books.utils.requests.get')
    def test_fetch_books_data_connection_error(self, mock_get):
        # Mocking a connection error
        mock_get.side_effect = requests.ConnectionError('Connection error')

        query = 'test'
        result = fetch_books_data(query)
        self.assertIsNone(result)

    @patch('books.utils.requests.get')
    def test_fetch_books_data_timeout(self, mock_get):
        # Mocking a timeout error
        mock_get.side_effect = requests.Timeout('Timeout error')

        query = 'test'
        result = fetch_books_data(query)
        self.assertIsNone(result)
