import requests
import json

latitude = 0.0
longitude = 0.0

def get_Position():
    global latitude,longitude
    api_endpoint2 ="http://api.open-notify.org/iss-now.json"

    response = requests.get(api_endpoint2)
    print(response.status_code)
    status =response.raise_for_status()
    print(status)
    ctype =response.headers['content-type']
    print(ctype)

    if response.status_code == 200 :
        print("success")
        data = response.json()
        print(json.dumps(data, indent=4))
        position = data["iss_position"]
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]
        pos = (position,latitude,longitude)
        print(pos)
    else :
        print("something went wrong!")
    

def get_SunriseSunset(lat ,long):
    api_endpoint2 ="https://api.sunrise-sunset.org/json"
    payload ={
        "lat" : lat ,
        "lng" : long
    }
    response = requests.get(api_endpoint2,params=payload)

    print(response.status_code)
    status =response.raise_for_status()
    ctype =response.headers['content-type']
    print(ctype)

    if response.status_code == 200 :
        data = response.json()
        print(json.dumps(data, indent=4))
        print(data)
        sunrise = data["results"]["sunrise"]
        sunset = data["results"]["sunset"]
        print("sunrise time is : " ,sunrise )
        print("sunset time is : " ,sunset )
    else :
        print("something went wrong!")


get_Position()
get_SunriseSunset(latitude,longitude)