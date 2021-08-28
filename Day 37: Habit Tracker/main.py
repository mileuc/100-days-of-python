import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("./.env")

TOKEN = os.getenv("TOKEN")
USERNAME = "mileuc"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# step 1: create user account on pixela - comment out once successful
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)  # check if successful or not

# step 2: create a new graph on pixela for our user name
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Sleep Habits Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# step 4 - Post value to the graph
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

yesterday = datetime(year=2021, month=6, day=7)
print(yesterday.strftime("%Y%m%d"))

today = datetime.now()
print(today.strftime("%Y%m%d"))

post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you sleep last night? ")
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(response.text)    # check https://pixe.la/v1/users/mileuc/graphs/graph1.html

# step 5 - update value with PUT
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_pixel_params = {
    "quantity": "7.25"
}

# response = requests.put(url=put_pixel_endpoint, json=put_pixel_params, headers=headers)
# print(response.text)

# step 6 - delete pixel with DELETE
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)