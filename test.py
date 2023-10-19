import csv
import requests
import unittest
from unittest.mock import patch
from url_checker import URLChecker

# Sample CSV file data for testing
CSV_DATA = [
    ['https://www.example.com'],
    ['https://www.invalidurl.com'],
    ['http://jogandocomelas.com.br/rosana-augusto-jogadora-do-santos-e-da-selecao-brasileira-anuncia-aposentadoria/'],
    ['http://sportv.globo.com/site/programas/rio-2016/noticia/2016/08/apos-vitoria-formiga-supera-cafu-em-jogos-pela-selecao-nunca-imaginei.html']
]

class URLCheckerTests(unittest.TestCase):
    @patch('url_checker.requests.get')
    def test_check_urls(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200

        url_checker = URLChecker('test_urls.csv')
        url_checker.check_urls()

        mock_get.assert_called_once_with('https://www.example.com')

    @patch('url_checker.requests.get')
    def test_check_urls_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException

        url_checker = URLChecker('test_urls.csv')
        url_checker.check_urls()

        # Check that requests.get is called with the correct URL
        mock_get.assert_called_once_with('https://www.invalidurl.com')

    def setUp(self):
        with open('test_urls.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(CSV_DATA)

    def tearDown(self):
        import os
        os.remove('test_urls.csv')

if __name__ == '__main__':
    unittest.main()