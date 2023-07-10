from tkinter import *
import random
from tkinter import messagebox
import pyperclip

# ---------------------------- Constant ------------------------------- #

FONT = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def genPassword():
    old_pwd = pwd_input.get()

    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', 
                 '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?']

    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    numbers =list(range(0,10))
    password = []
    pwd = ""
    for num in range(1,6):
        password.append(str(random.choice(numbers)))
    for char in range(1,6):
        password.append(random.choice(special_chars))
    for alpha in range(1,6):
        password.append(random.choice(alphabets))
    random.shuffle(password)

    for paswd in password :
        pwd += paswd

    # it will delete all the text from textbox from position 0 to end.
    pwd_input.delete(0,END)
    # it will insert the text start from posiion 0
    pwd_input.insert(0,pwd)
    pyperclip.copy(pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def saveData():
    website = web_input.get()
    email = email_input.get()
    password = pwd_input.get()
    data = website + "|" + email + "|" + password + "\n"

    
    
    response = messagebox.askokcancel(title="Verifty entered details" ,message=f"website : {website}\n email : {email}\n password : {password}")
    if response :
        new =Label()
        if len(website)<=0 :
            web_resp = messagebox.showinfo(title="web Validation" , message="Please enter website name")
        if len(email) <= 0 :
            email_resp = messagebox.showerror(title="email Validation" , message="Please enter email address")
        if  len(password) <= 0:
            pwd_resp = messagebox.showerror(title="pwd Validation" , message="Please enter password")
        
        if len(website) & len(email) & len(password) > 0 :
            try :
                with open("files/tkintergui/password-manager/data.txt","+a") as file :
                    file.write(data)
            except FileNotFoundError as error:
                # block executed if try block caused exception
                new.config(text=f"{error}Opps ! something went wrong." ,fg="red")
                new.grid(row=7)
            else :
                 # block executed if try block not caused exception
                web_input.delete(0,END)
                email_input.delete(0,END)
                pwd_input.delete(0,END)
                new.config(text="Record added successfully.",fg="green")
                new.grid(row=7)
            finally :
                print("All works well")
    print(website,email,password)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.geometry("700x500")
window.title("Password Manager")
window.config(padx=20,pady=20,bg="white")


canvas = Canvas()
canvas.config(width=250,height=250,highlightthickness=0,bg="white")
image_url = PhotoImage(file="files/tkintergui/password-manager/logo.png")
canvas.create_image(125,125,image=image_url)
canvas.grid(column=1,row=0)


#website

web_label = Label()
web_label.config(text="Website",font=(FONT,20,"bold"),fg="black" ,bg="white")
web_label.grid(column=0,row=2)

web_input =Entry()
web_input.config(text="Enter Website Name ",fg="black",bg="white",width=30, highlightthickness=0,highlightbackground="white")
web_input.focus()
web_input.grid(column=1,row=2,columnspan=2)



#Email/Username

email_label = Label()
email_label.config(text="Email/Username",font=(FONT,20,"bold"),fg="black" ,bg="white")
email_label.grid(column=0,row=3)

email_input =Entry()
email_input.config(text="Enter Email/Username ",fg="black",bg="white",width=30,highlightthickness=0,highlightbackground="white")
email_input.insert(0,"yogesh.dhameliya6013@gmail.com")
email_input.grid(column=1,row=3,columnspan=2)


#Password
pwd_label = Label()
pwd_label.config(text="Password",font=(FONT,20,"bold"),fg="black" ,bg="white")
pwd_label.grid(column=0,row=4)

pwd_input =Entry()
pwd_input.config(text="Enter Password ",fg="black",bg="white",width=30,highlightthickness=0,highlightbackground="white")
pwd_input.grid(column=1,row=4,columnspan=2)

#gen pwd
pwd_gen = Button()
pwd_gen.config(text="Generate Password",command= genPassword,fg="black",bg="white",width=15,highlightthickness=0,highlightbackground="white")
pwd_gen.grid(column=2,row=5)

#save

save = Button()
save.config(text="Save",command=saveData,fg="black",bg="white",highlightthickness=0,width=15,highlightbackground="white")
save.grid(column=1,row=5)
window.mainloop()

