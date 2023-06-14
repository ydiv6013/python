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

    fname = fname_input.get()
    mname = mname_input.get()
    lname = lname_input.get()
    numerology ={
        1:['A','J','S'],
        2:['B','T','K'],
        3:['L','C','U'],
        4:['M','D','V'],
        5:['N','E','W'],
        6:['O','F','X'],
        7:['P','G','Y'],
        8:['Q','H','Z'],
        9:['R','I'],
    }

    numerology1 =[
        [''],
        ['A','J','S'],
        ['B','T','K'],
        ['L','C','U'],
        ['M','D','V'],
        ['N','E','W'],
        ['O','F','X'],
        ['P','G','Y'],
        ['Q','H','Z'],
        ['R','I'],
    ]

    print(numerology1[1])
    fname_total = 0
    mname_total = 0
    lname_total = 0
    final_number = 0

    for i in fname :
        print(i)
        for j in numerology[8]:
            print(j)

    '''

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
'''

    
# ------------------------- Window UI------------------------------------#
window = Tk()
window.geometry("500x600")
window.title("Life Path Number")
window.config(padx=50,pady=50,bg=YELLOW)


# Full Name
label= Label()
label.config(text="Destiny Number",fg="black",bg=YELLOW,font=(FONT_NAME,20,"bold"),pady=20)
label.grid(column=1,row=0,columnspan=2)

#first name
fname_label= Label()
fname_label.config(text="First Name",fg="black",bg=YELLOW,font=(FONT_NAME,20,"bold"))
fname_label.grid(column=1,row=1)

fname_input = Entry()
fname_input.config(text="fname" ,bg=YELLOW)
fname_input.grid(column=2,row=1)

#Middle name
mname_label= Label()
mname_label.config(text="Middle Name",fg="black",bg=YELLOW,font=(FONT_NAME,20,"bold"))
mname_label.grid(column=1,row=2)

mname_input = Entry()
mname_input.config(text="mname",bg=YELLOW)
mname_input.grid(column=2,row=2)

#last name
lname_label= Label()
lname_label.config(text="Last Name",fg="black",bg=YELLOW,font=(FONT_NAME,20,"bold"))
lname_label.grid(column=1,row=3)

# Dob input

lname_input = Entry()
lname_input.config(text="lname" ,bg=YELLOW)
lname_input.grid(column=2,row=3)


submit =Button()
submit.config(text="Submit",command=findNumber,fg="black",bg=YELLOW,width=15,highlightthickness=0,highlightbackground=YELLOW)
submit.grid(column=1,row=4,columnspan=2)
window.mainloop()