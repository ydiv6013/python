import random as rn
import pandas as pd

countries = [ "Finland","Norway","Denmark","Iceland","Switzerland","Netherlands","Canada"]

countries_with_rank = {country:rn.randint(1,10) for country in countries}

print(countries_with_rank)

country = {country:rank for (country,rank) in countries_with_rank.items() if rank >=5}
print(countries_with_rank.items())
print(country)

sentence = "Learning a little each day adds up. Research shows that students who make learning a habit are more likely to reach their goals. Set time aside to learn and get reminders using your learning scheduler."

word_length = {word:len(word) for word in sentence.split()}

print(word_length,len(word_length))

word_length2 = {word:len(word) for word in sentence.split() if len(word) >= 5}

print(word_length2,len(word_length2))

filehandle = open("files/top-10-country-temp.csv")
lines = filehandle.readlines()
country_temp  = {
    "Country" : [],
    "temp" : []
}

country = [ ]
temp = [ ]

for data in lines:
    data_list = data.split(",")
    country_name = data_list[0]
    country.append(country_name)
    temp_list= data_list[1].split('\n')
    temprature =temp_list[0]
    temp.append(temprature)
    
    
country_temp = {
    "country" : country,
    "ftemp" : temp
}

country_cel_temp =[round((float(ftemp)-32)*(5/9),2) for ftemp in temp]
print("\n cel temp : \n",country_cel_temp)

cont = pd.DataFrame(country_temp)


print(cont)
print(cont.loc[:,"country"])
print(cont.loc[:,"ftemp"])

for (key, value) in cont.items():
    print(key)
    print(value)

for (index,row) in cont.iterrows():
    print(index)
    print(row)
    print(row.country)
    print(row.ftemp)
