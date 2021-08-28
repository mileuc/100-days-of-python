import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv("./.env")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
sheety_headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
}

class DataManager:
    def __init__(self):
        self.destination_records = {}

    def acquire_records(self):
        sheety_get_response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
        sheety_get_result = sheety_get_response.json()
        print(sheety_get_result)
        self.destination_records = sheety_get_result["prices"]
        # pprint(self.destination_records)  # formats the JSON to make it more readable

        # pass everything in the prices key back to main.py and store it in a variable
        return self.destination_records

    def update_records(self, updated_records):
        for record in updated_records:
            sheety_put_params = {
                "price": record
            }

            sheety_put_response = requests.put(url=f"{SHEETY_ENDPOINT}/{record['id']}", json=sheety_put_params,
                                               headers=sheety_headers)
            # print(sheety_put_response.text)

