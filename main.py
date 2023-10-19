import csv
import requests

class URLChecker:
    def __init__(self, file_path):
        self.file_path = file_path

    def check_urls(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                url = row[0]
                self.check_url(url)

    def check_url(self, url):
        try:
            response = requests.get(url)
            status_code = response.status_code
            print(f"({status_code}) {url}")
        except requests.exceptions.RequestException:
            print(f"(Error) {url}")

url_checker = URLChecker('Task 2 - Intern.csv')
url_checker.check_urls()