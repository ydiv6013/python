import requests
from datetime import date

TOKEN = str(input("please enter token :" ))
USERNAME = str(input("please enter user name :"))
pixela_endpoints = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs"
graph_id = "graph1"
graph_headers = {
        "X-USER-TOKEN" : TOKEN
    }

def create_user() :
    # step 1 : Create your user account
    user_params ={
        "token" :  TOKEN,
        "username" : USERNAME ,
        "agreeTermsOfService" : "yes" ,
        "notMinor" : "yes" 
    }
    response = requests.post(url=pixela_endpoints , json=user_params)
    print("Response is " ,response)
    print(" json Response is \n",response.json)
    print("Text Response is \n",response.text)

def create_graph() :
    # step 2 : Create a graph definition
    # https://pixe.la/v1/users/a-know/graphs

    
    
    print(graph_headers)
    graph_body = {
        "id" : graph_id ,
        "name" : " Cycling graph" ,
        "unit" : "kilogram" ,
        "type" : "float" ,
        "color" : "ajisai" 

    }
    graph_response = requests.post(url=graph_endpoint, 
                                json=graph_body,
                                headers=graph_headers)
    print(graph_response)
    print(graph_response.text)

def get_graph() :
    # step 3 : Get the graph!

    print("link to browse created graph" ,f"{pixela_endpoints}/{USERNAME}/graphs/graph1.html")

def add_pixel_value() :

    # step 4 : Post value to the graph

    graphvalue_endpoint = f"{graph_endpoint}/{graph_id}"

    today = date.today()
    today_year = str(today.year)
    today_day = str(today.day)
    today_month = str(today.month)

    if(len(today_month)) == 1 :
        today_month= f"0{today_month}"
    if(len(today_day)) == 1 :
        today_day= f"0{today_day}"

    current_date =f"{today_year}{today_month}{today_day}"
    qty = input("Specify the quantity to be registered on the specified date")
    graphvalue_body = {
        "date" : current_date ,
        "quantity" : qty ,
    }
    graphvalue_response = requests.post(url=graphvalue_endpoint,
                                        json=graphvalue_body,
                                        headers=graph_headers)

    print(graphvalue_response)
    print(graphvalue_response.text)




def update_pixel_value():
    # update a graph value
    qty = input("enter qty")
    date = input("enter date to update pixel in yyyymmdd : " )
    endpoint = f"{pixela_endpoints}/{USERNAME}/graphs/{graph_id}/{date}"
    updatevalue_body = {
        "quantity" : qty ,
    }

    response = requests.put(url=endpoint,json=updatevalue_body,headers=graph_headers)
    print(response.text)

def delete_user() :
    
    username = input("enter username to delete user")
    endpoint =f"{pixela_endpoints}/{username}"
    response = requests.delete(url=endpoint,headers=graph_headers)
    print(response.text)

#create_user()
#create_graph()
#get_graph()
#add_pixel_value() 
#update_pixel_value()
delete_user()