# sign up form using tkinter gui 

from tkinter import *

window= Tk()
#window.minsize(width=700,height=600)

#Set the geometry of tkinter frame
window.geometry("500x600")
window.title("Sign Up")
window.config(padx=20,pady=20)


#Sign Up Form
name = Label()
name.config(text="Name : ",font=("Times New Roman",18,"bold"),fg="Black")
name.grid(column=0,row=1)

name_input = Entry()
name_input.config(text="name", fg="black", bg="white")
name_input.grid(column = 1,row = 1)




email = Label()
#email.pack()
email.config(text="Email : " ,font=("Times New Roman",18,"bold"), fg="black")
email.grid(column=0,row=2)

email_input = Entry()
#email_input.pack()
email_input.config(text="email", fg="black", bg="white")
email_input.grid(column=1,row=2)

pwd = Label()
pwd.config(text="Password : " ,font=("Times New Roman",18,"bold"), fg="black")
pwd.grid(column=0,row=3)

pwd_input = Entry()
pwd_input.config(text="password", fg="black", bg="white")
pwd_input.grid(column=1,row=3)

language = Label()

language.config(text="Languages Known : ",font=("Times New Roman",18,"bold"),fg="Black")
language.grid(column=0,row=4)
#checkboox

checkvar1 = IntVar()  
checkvar2 = IntVar()  
checkvar3 = IntVar()  
  
chkbtn1 = Checkbutton()
chkbtn2 = Checkbutton()
chkbtn3 = Checkbutton()

chkbtn1.config(text = "C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 1, width = 5 ,fg="black")  
chkbtn2.config(text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 1, width = 5,fg="black")  
chkbtn3.config(text = "Java", variable = checkvar3, onvalue = 1, offvalue = 0, height = 1, width = 5,fg="black")  

chkbtn1.grid(column=1,row=4)
chkbtn2.grid(column=1,row=5)
chkbtn3.grid(column=1,row=6)



# Gender
gender = Label()
#gender.pack()
gender.config(text="Gender : ",font=("Times New Roman",18,"bold"),fg="Black")
gender.grid(column=0,row=7)
#Radiobox

gen = IntVar()  

male = Radiobutton()
female = Radiobutton()

male.config(text="Male",variable=gen,value=1 , fg="black")
female.config(text="Female",variable=gen ,value=2,fg="black")

male.grid(column=1,row=7)
female.grid(column=1,row=8)




# Country
country = Label()
country.config(text="Select Country : ",font=("Times New Roman",18,"bold"),fg="Black")
country.grid(column=0,row=9)
#ListBox

country_listbox =Listbox()
#country_listbox.pack()
country_listbox.config(fg="black" ,bg="white", height=4)

country_list =["India","USA","Japan","Austrelia"]

for items in country_list:
    country_listbox.insert(country_list.index(items),items)
country_listbox.grid(column=1,row=9)




def on_submit():
    name = name_input.get()
    email = email_input.get()
    pwd = pwd_input.get()
    c = checkvar1.get()
    cplus = checkvar2.get()
    java = checkvar3.get()
    gender =gen.get()
    countrylist = country_listbox.get(country_listbox.curselection())

    credentials = name + "\n" + email + "\n" + "\n" +pwd + str(c) + str(cplus) + str(java) +"Gender\n"+str(gender)+"\n"+countrylist

    cred = Label()
    cred.config(text=credentials,fg="black")
    cred.grid(column=1,row=11)

btn = Button()
btn.config(text="Submit",fg="black",command=on_submit)
btn.grid(column=1,row=10)







window.mainloop()
exit()

