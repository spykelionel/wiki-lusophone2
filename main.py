import csv
import requests

# Open the CSV file
with open('Task 2 - Intern.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if present

    # Process each row in the CSV file
    for row in reader:
        url = row[0]  # Assuming the URL is in the first column

        try:
            response = requests.get(url)
            status_code = response.status_code
            print(f"({status_code}) {url}")
        except requests.exceptions.RequestException:
            print(f"(Error) {url}")