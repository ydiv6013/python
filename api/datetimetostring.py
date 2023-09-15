
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

today_date = now.strftime("%m/%d/%Y")
print("current date : ",today_date )

current_time = now.strftime("%H:%M:%S")
print("current time : ",current_time )




    