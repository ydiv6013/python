import pandas as pd


try :
    data = pd.read_csv("files/Central_Park_Squirrel_Census_Squirrel_Data.csv")
except:
    print("No such file found")


color = "Primary Fur Color"
gray = data[data[color] == "Gray"]
cinnamon = data[data[color] == "Cinnamon"]
black = data[data[color] == "Black"]

gray_count = len(gray)
cinnamon_count = len(cinnamon)
black_count = len(black)


data_dict ={
    "Primary Fur Color" : ["Gray","Cinnamon","Black"],
    "count" :[gray_count,cinnamon_count,black_count]
}

print(data_dict)

# create a csv file 

dataframe = pd.DataFrame(data_dict)
print(dataframe)

try :
    dataframe.to_csv("files/squireel_count.csv")
except: 
    print("Opps ,something went wrong !")
    

