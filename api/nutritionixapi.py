#https://sheety.co

import requests
from datetime import datetime

APP_ID = "7deb8bcb"
API_KEY = "413fc8134641c27cd09eb74fe9d740db"

excercise = input("which excercise you did today : ")

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
excercise_header={
        "x-app-id" :  APP_ID,
        "x-app-key" : API_KEY
    }
excercise_body ={
    "query": excercise,
    "gender":"female",
    "weight_kg":72.5,
    "height_cm":167.64,
    "age":30
}

response = requests.post(url=excercise_endpoint,
                         json=excercise_body,
                         headers=excercise_header)

result = response.json()
print(response)
print(response.json)
print(response.text)


sheety_endpoint = "https://api.sheety.co/01b39e2cabeae06a7b2846cc3722ad50/myWorkouts/workouts"

auth_credentials = ("yogesh6013","Yogesh@6013")

now = datetime.now()

today_date = now.strftime("%m/%d/%Y")
print("current date : ",today_date )

current_time = now.strftime("%H:%M:%S")
print("current time : ",current_time )


for excercise in result["exercises"] :
    print(excercise)
    name = excercise["name"]
    duration = excercise["duration_min"]
    calories = excercise["nf_calories"]
    print("name is : ",name)
    print("duration is : ",duration)
    print("calories is : ",calories)

    sheety_body ={
        "workout" : {
            "date" : today_date,
            "time" : current_time,
            "exercise" : name,
            "duration" : duration,
            "calories" : calories
        },
    }
    sheety_response = requests.post(url=sheety_endpoint,
                                    json=sheety_body,
                                    auth= auth_credentials)
    print(sheety_response.text)