import requests 
import json

question_data =[]

def fetchData():
    global question_data
    #https://opentdb.com/api.php?amount=10&type=boolean
    endpoint ="https://opentdb.com/api.php"

    payload ={
        "amount" : 10 ,
        "type" : "boolean"
    }
    
    response = requests.get(endpoint,params=payload)
    status = response.status_code
    print(response,status)

    if status == 200 :
        data = response.json()
        print(json.dumps(data,indent=4))
        question_data =data["results"]
        
    else :
        print("Opps something went wrong")


fetchData()
