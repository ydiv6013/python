# using pandas

import pandas

try :
    data = pandas.read_csv("files/happinessindex.csv")  
except :
    print("No such file found")

country ="Country or region"
print(data[country].to_list())

#print country data whose score is maximum
print("max is : \n")
print(data[data.Score == data.Score.max()])

gdp ="GDP per capita"
maxgdp = data[gdp].max()
print(maxgdp)
print(data[data[gdp] == data[gdp].max()])