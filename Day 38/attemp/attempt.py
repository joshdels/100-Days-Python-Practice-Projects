import requests
from datetime import datetime
import os

now = datetime.now()
date_format = now.strftime("%d/%m/%Y")
time_format = now.strftime("%X")

print(date_format)
print(time_format)

NUTRITION_APPLICATION_ID = os.environ.get('NUTRITION_APPLICATION_ID')
NUTRITION_API_KEY = os.environ.get('NUTRITION_API_KEY')
NUTRITION_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_END_POINT = os.environ.get('SHEETY_END_POINT')


headers = {
    "x-app-id": NUTRITION_APPLICATION_ID,
    "x-app-key": NUTRITION_API_KEY
}

query_params = {
    "query": str(input("What did you do today? "))
}

response = requests.post(url=NUTRITION_END_POINT, json=query_params, headers=headers)
data = response.json()

print(data)

for exercise in data["exercises"]:
    sheety_params = {
        "workout" : {
            "date": date_format,
            "time": time_format,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_response = requests.post(url=SHEETY_END_POINT, json=sheety_params)
print(sheety_response.text)


# the for loop is terrible dyem
