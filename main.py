import csv
import requests

with open('Task 2 - Intern.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        url = row[0]  
        try:
            response = requests.get(url)
            status_code = response.status_code
            print(f"({status_code}) {url}")
        except requests.exceptions.RequestException:
            print(f"(Error) {url}")
