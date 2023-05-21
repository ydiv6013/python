# Python access csv file 
import csv
import pandas

class Weathercsv :
    ''' Uses python csv library to access csv data'''
    def __init__(self) -> None:
        pass
    
    def readWeatherdata(self):
        temprature = []
        temprature1 = []
        try:
            filehandler = open("weather_data.csv")
            content = csv.reader(filehandler)
            for row in content :
                print(row)
                print(row[1])
                temprature.append(row[1])
                if row[1] != 'temp' :
                    temprature1.append(row[1])

            print(temprature)
            print(temprature1)
            filehandler.close()
        except :
            print("No such file found")
        
class Weather :
    ''' access python csv data'''
    def __init__(self) -> None:
        pass

    def readWeatherData(self):
        try :
            filehandler = open("weather_data.csv")
            content = filehandler.read()
            data = content.split()
            for row in data:
                print(row)
            filehandler.close()
        except:
            print("No such File found")


# read csv using python pandas

class WeatherPandas:
    def __init__(self) -> None:
         pass
    def readPandascsv(self):
        data = pandas.read_csv("weather_data.csv")
        print(data)
        print("Temprature is :\n",data["temp"])
        print("Day is :\n",data["day"])
        print("Conditions is :\n",data["condition"])

        print(type(data))
        print(type(data["day"]))

        data_dict = data.to_dict()
        print(data_dict)

        data_json = data.to_json()
        print(data_json)
        
        series_day_dict = data["day"].to_dict()
        print(series_day_dict)

        series_day_list = data["day"].to_list()
        print(series_day_list)
        series_temp_list = data["temp"].to_list()
        print(series_temp_list)
        series_condition_list = data["condition"].to_list()
        print(series_condition_list)

        #find the avg temprature of temp column
        total = 0
        length =len(data["temp"])
        for x in data["temp"]:
            total = total + x
            avg = total/length
           
        print("Total avg of tmp is : ",round(avg,2))

        #find the maximum temprature

        maximum = data["temp"].max()
        print("maximum temp is : ",maximum)

        #find the minimum temprature


        minimum = data["temp"].min()
        print("minimum temp is : ",minimum)

    def ctoh(self):
        # convert Celsius to Fahrenheit
        data = pandas.read_csv("weather_data.csv")
        celsius = data["temp"].to_list()
        fahrenheit_list =[]
        for x in celsius :
            print(x)
            fahrenheit = (float(x) * (9/5) ) + 32
            fahrenheit_list.append(fahrenheit)

        print(fahrenheit_list)
        print(fahrenheit)

        


weather = Weather()
weather.readWeatherData()

weathercsv = Weathercsv()
weathercsv.readWeatherdata()

weatherpandas = WeatherPandas()
weatherpandas.readPandascsv()
weatherpandas.ctoh()
