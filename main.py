import requests
from datetime import datetime
import os

GENDER = "MALE"
WEIGHT_KG = "52"
HEIGHT_CM = "160"
AGE = "26"

APP_ID = "68b35fd8"
API_KEY = "358be9dd1490362bb912698f2727a7b9"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/9e3ac95a129d593e589ea4f552c3b407/workoutTracking/workouts"

exercise_input = input("Tell me which exercise you did today?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_params = {
    "query": "exercise_input",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}


response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
# response.raise_for_status()
result = response.json()
print(result)

today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # bearer_headers = {
    #     "Authorization": "Bearer Iamreallycuteandbeautiful!"
    # }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)
    print(sheet_response.text)