import pandas as pd
data2 = pd.read_csv("files/happinessindex.csv")
country = "Country or region"
rank = "Overall rank"

'''

print(data2["Country or region"].describe())
print(data2["Healthy life expectancy"].describe())

print(data2["Country or region"].unique())
print(data2["Country or region"].value_counts())

'''
hle_mean= data2["Healthy life expectancy"].mean()
print(hle_mean)
hle_mean_map = data2["Healthy life expectancy"].map(
                lambda p : p / hle_mean)

print(hle_mean_map)

print(data2["Country or region"].value_counts())
country_group = data2.groupby(country).count()
country_group_min = data2.groupby(rank).min()

print(country_group)
print(country_group_min)
print(data2.groupby([country]).rank.agg([len,min,max]))

exit()
#  there are two pandas core object 1.DataFrame ,2.Series
dict = pd.DataFrame({
        "Name" : ["Yogesh","Hiren"],
        "Age" : [32,31]
    },
    index= ["Data1","Data2"]
)

print(dict)


dict1=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
                    'Sue': ['Pretty good.', 'Bland.']})
print(dict1)


se1=pd.Series([30, 35, 40], 
              index=['2015 Sales', '2016 Sales', '2017 Sales'], 
              name='Product A')
print(se1)

#index_col = 0 uses index of the csv rather then creating a new one
data = pd.read_csv("files/countrygdp.csv",index_col=0)



#shape gives tuples(num of rows,num of columns)

print(data.shape)

print(data.head)

# return record from Country column positioned at 0.
print(data['Country'][0])

print(data.iloc[:,1])
print(data.iloc[10,1])
print(data.iloc[:3,0])
print(data.iloc[10:30,0])

print(data.iloc[[12,15,17,20,22,25,90]])
print(data.iloc[-5:])


print(data.loc[0,'Country'])
print(data.loc[:10,'Country'])
print(data.loc[:5,'Country'])


data2 = pd.read_csv("files/happinessindex.csv")

print(data2.loc[:10,["Country or region","GDP per capita",
                     "Healthy life expectancy"]])

print(data2.loc[10:15,["Country or region","GDP per capita",
                     "Healthy life expectancy"]])

print(data2.loc[:,["Country or region","GDP per capita",
                "Healthy life expectancy"]])
print(data2.set_index("Overall rank"))

print(data2["Country or region"] == "Switzerland")

print(data2["Country or region"].isin(["Switzerland","Yemen"]))


