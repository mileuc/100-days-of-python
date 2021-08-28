"""
OpenAI's GPT-3 AI Model: NLP Model where if you ask a question, it can search through all of the text and
find the relevant part.

We'll write down the exercises we did in a normal english sentence.
    eg. ran 5k and cycled for 20 minutes.
Run the code, and then the data should be logged into a Google Spreadsheet.
Both activities mentioned should be logged and it should figure out the duration based on the distance for
running. For the cycling, the duration is directly mentioned and should log 20 minutes.
It should also work out the number of calories expended.

Will also use: Python DateTime strftime() method.
APIs and making POST requests
Creating authorization headers and environment variables
"""

import requests
import os
from dotenv import load_dotenv
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 178
AGE = 26

PROJECT_NAME = "workingTracking"
SHEET_NAME = "workouts"

load_dotenv("./.env")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")

user_input = input("What exercises have you done today? ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
    "query": f"{user_input}",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

# print exercise stats for a plain text input for using the Nutritionix "Natural Language for Exercise" API
nutritionix_response = requests.post(url=exercise_endpoint, json= exercise_params, headers=nutritionix_headers)
nutritionix_result = nutritionix_response.json()
print(nutritionix_result)

# use Sheety API to generate a new row of data in Google Sheet for each exercise from the Nutritionix API
# the date and time columns should contain the current date and time from the Python datetime module
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

today = datetime.now()
# print(today)

for exercise in nutritionix_result["exercises"]:
    sheety_params = {
      "workout": {
          "date": today.strftime("%d/%m/%Y"),
          "time": today.strftime("%X"),
          "exercise": exercise["user_input"].title(),
          "duration": exercise["duration_min"],
          "calories": exercise["nf_calories"]
      }
    }

    # using bearer token authentication
    sheety_header = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_header)
    print(sheety_response.text)