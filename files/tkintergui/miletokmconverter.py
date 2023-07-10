from tkinter import *

window = Tk()
#Set the geometry of tkinter frame
window.geometry("500x600")
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

def onSubmit():
    mile = float(mile_input.get())
    km = round(mile * 1.609344,2)
    km_lable2.config(text=km,fg="black")
   

mile_input = Entry()
mile_input.config(text="Enter Mile",fg="black",bg="white")
mile_input.grid(column=1,row=2)

mile_lable =Label()
mile_lable.config(text="Miles",font=("Times New Roman",18,"bold"), fg="black")
mile_lable.grid(column=2,row=2)

km_lable =Label()
km_lable.config(text="is equal to ",font=("Times New Roman",18,"bold"), fg="black")
km_lable.grid(column=1,row=3)



km_lable2 =Label()
km_lable2.config(text=" ",font=("Times New Roman",18,"bold"), fg="black")
km_lable2.grid(column=2,row=3)


km_lable3 =Label()
km_lable3.config(text=" km",font=("Times New Roman",18,"bold"), fg="black")
km_lable3.grid(column=3,row=3)

submit =Button()
submit.config(text="Submit",fg="black", command=onSubmit)
submit.grid(column=2,row=4)
window.mainloop()