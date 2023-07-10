#python program using pandas to create a csv with country name and gdp

import pandas

try:
    data = pandas.read_csv("files/happinessindex.csv")
except:
    print("Opps ,Something went wrong!")


#extract a data from csv
gdp = "GDP per capita"
country ="Country or region"
gdp_list = data[gdp].to_list()
country = data[country].to_list()

data_dict ={
    "Country" : country ,
    "GDP" :gdp_list
}

print(data_dict)

dataframe = pandas.DataFrame(data_dict)

print(dataframe)
dataframe.to_csv("files/countrygdp.csv")