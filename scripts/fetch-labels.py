import os
import requests
import csv
from dotenv import load_dotenv

# This script is used to fetch the current list of labels and store as CSV.
# The file can then be displayed in the tech docs.

load_dotenv()

# Get PHQ API Token from env
PHQ_API_TOKEN = os.getenv("PHQ_API_TOKEN")


def fetch_and_store_labels():
    response = requests.get(
        "https://api.predicthq.com/v1/events/count/",
        headers={
            "Authorization": f"Bearer {PHQ_API_TOKEN}",
        },
    )

    # Checking if the response is OK
    if response.status_code == 200:
        data = response.json()

        legacy_labels = list(data["labels"].keys())
        phq_labels = list(data["phq_labels"].keys())

        # Ensure labels are sorted
        legacy_labels.sort()
        phq_labels.sort()

        # Write legacy labels to CSV
        with open("assets/legacy-labels.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for label in legacy_labels:
                writer.writerow([label])

        # Write PHQ labels to CSV
        with open("assets/phq-labels.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for label in phq_labels:
                writer.writerow([label])

        print("Success")
    else:
        print(f"Failed to fetch labels, status code: {response.status_code}")


if __name__ == "__main__":
    fetch_and_store_labels()
