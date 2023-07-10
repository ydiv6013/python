from tkinter import *
import math



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"



# ------------------------- Find Number------------------------------------#
def findNumber():

    day = day_input.get()
    month = month_input.get()
    year = year_input.get()
    day_total = 0
    month_total = 0
    year_total = 0
    final_number = 0
    for i in day:
        day_total += int(i)

    for i in month:
        month_total += int(i)

    for i in year:
        year_total += int(i)

    total_sum_dob = str(day_total + month_total + year_total)


    if len(total_sum_dob) > 9 :
        
        for i in total_sum_dob :
            final_number += i
    else :
        for i in total_sum_dob :
            final_number  += int(i)

    lpn_label = Label()
    lpn_label.config(text=f"Date : {day_total}\n Month : {month_total}\n Year : {year_total}\n Total Number :{total_sum_dob , final_number}",pady=10,bg=YELLOW)
    lpn_label.grid(column=1,row=5,columnspan=2)

    lpn_label1 = Label()
    lpn_label1.config(text=f"Your Life Path Number :{final_number}",pady=10,bg=YELLOW)
    lpn_label1.grid(column=1,row=6,columnspan=2)


    
# ------------------------- Window UI------------------------------------#
window = Tk()
window.geometry("500x600")
window.title("Life Path Number")
window.config(padx=50,pady=50,bg=YELLOW)


# Date of Birth
label= Label()
label.config(text="Life Path Number",fg="black",bg=YELLOW,font=(FONT_NAME,20,"bold"),pady=20)
label.grid(column=1,row=0,columnspan=2)
#Day
day_label= Label()
day_label.config(text="day",fg="black",bg=YELLOW,font=(FONT_NAME,20,"bold"))
day_label.grid(column=1,row=1)

# Dob input

day_input = Entry()
day_input.config(text="day" ,bg=YELLOW)
day_input.grid(column=2,row=1)

#Month
month_label= Label()
month_label.config(text="month",fg="black",bg=YELLOW,font=(FONT_NAME,20,"bold"))
month_label.grid(column=1,row=2)

# Month input

month_input = Entry()
month_input.config(text="month",bg=YELLOW)
month_input.grid(column=2,row=2)


#Day
year_label= Label()
year_label.config(text="year",fg="black",bg=YELLOW,font=(FONT_NAME,20,"bold"))
year_label.grid(column=1,row=3)

# Dob input

year_input = Entry()
year_input.config(text="year" ,bg=YELLOW)
year_input.grid(column=2,row=3)


submit =Button()
submit.config(text="Submit",command=findNumber,fg="black",bg=YELLOW,width=15,highlightthickness=0,highlightbackground=YELLOW)
submit.grid(column=1,row=4,columnspan=2)
window.mainloop()