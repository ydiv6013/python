# sign up form using tkinter gui 

from tkinter import *

window= Tk()
#window.minsize(width=700,height=600)

#Set the geometry of tkinter frame
window.geometry("700x600")
window.title("Sign Up")


#Sign Up Form
header =Label()
header.pack(side="top")
header.config(text="SignUp Form",font=("Times New Roman",38,"bold"),fg="black")
name = Label()
#name.pack()
name.config(text="Name : ",fg="Black")
name.place(x=20,y=20)

name_input = Entry()
#name_input.pack()
name_input.config(text="name", fg="black", bg="white")
name_input.place(x=100,y=20)

email = Label()
#email.pack()
email.config(text="Email : " , fg="black")
email.place(x=20,y=70)

email_input = Entry()
#email_input.pack()
email_input.config(text="email", fg="black", bg="white")
email_input.place(x=100,y=70)


pwd = Label()
#pwd.pack()
pwd.config(text="Password : " , fg="black")
pwd.place(x=20,y=120)

pwd_input = Entry()
#pwd_input.pack()
pwd_input.config(text="password", fg="black", bg="white")
pwd_input.place(x=100,y=120)




language = Label()
#language.pack()
language.config(text="Languages Known : ",fg="Black")
language.place(x=20,y=170)
#checkboox

checkvar1 = IntVar()  
checkvar2 = IntVar()  
checkvar3 = IntVar()  
  
chkbtn1 = Checkbutton()
chkbtn2 = Checkbutton()
chkbtn3 = Checkbutton()

#chkbtn1.pack()    
#chkbtn2.pack()  
#chkbtn3.pack()  

chkbtn1.config(text = "C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 1, width = 5 ,fg="black")  
chkbtn2.config(text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 1, width = 5,fg="black")  
chkbtn3.config(text = "Java", variable = checkvar3, onvalue = 1, offvalue = 0, height = 1, width = 5,fg="black")  

chkbtn1.place(x=150,y=150)
chkbtn2.place(x=150,y=180)
chkbtn3.place(x=150,y=210)

# Gender
gender = Label()
#gender.pack()
gender.config(text="Gender : ",fg="Black")
gender.place(x=20,y=250)
#checkboox

gen = IntVar()  

male = Radiobutton()
female = Radiobutton()

male.pack()
female.pack()

male.config(text="Male",variable=gen,value=1 , fg="black")
female.config(text="Female",variable=gen ,value=2,fg="black")

male.place(x=150,y=250)
female.place(x=220,y=250)

# Country
country = Label()
#country.pack()
country.config(text="Select Country : ",fg="Black")
country.place(x=20,y=300)
#ListBox

country_listbox =Listbox()
#country_listbox.pack()
country_listbox.config(fg="black" ,bg="white", height=4)
country_listbox.insert(1,"India")
country_listbox.insert(2, "USA")  
country_listbox.insert(3, "Japan")  
country_listbox.insert(4, "Austrelia")  

country_listbox.place(x=150,y=300)



# Favourtite Fruites
fruites = Label()
#fruites.pack()
fruites.config(text="Select Favourite Fruites : ",fg="Black")
fruites.place(x=20,y=380)
#ListBox

fruites_listbox =Listbox()
#fruites_listbox.pack()
fruites_listbox.config(fg="black",bg="white", height=4)
fruites_list =["Apple","Mango","Banana","Orange","Grapes"]

for items in fruites_list:
    fruites_listbox.insert(fruites_list.index(items),items)
 

fruites_listbox.place(x=150,y=420)

def on_submit():
    name = name_input.get()
    email = email_input.get()
    pwd = pwd_input.get()
    c = checkvar1.get()
    cplus = checkvar2.get()
    java = checkvar3.get()
    gender =gen.get()
    countrylist = country_listbox.get(country_listbox.curselection())
    fruiteslist =fruites_listbox.get(fruites_listbox.curselection())

    credentials = name + "\n" + email + "\n" + "\n" +pwd + str(c) + str(cplus) + str(java) +"Gender\n"+str(gender)+"\n"+countrylist+"\n"+fruiteslist

    cred = Label()
    cred.pack(side="left")
    cred.config(text=credentials,fg="black")
    cred.place(x=320,y=100)

btn = Button()
btn.pack()
btn.config(text="Submit",fg="black",command=on_submit)
btn.place(x=150,y=550)




window.mainloop()