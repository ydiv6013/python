from tkinter import *

# TK() will initialize the window
window = Tk()

window.title("Python GUI Program")
window.minsize(width=350,height=350)


# multiple arguments
def add(*args):
    print(type(args),args)
    print(args[0],args[3])
    a = args[4]
    b = args[5]
    c = args[6]
    sum = 0

    add = a + b + c
    print(f"addition of a= {a},b = {b},c = {c} is : {add}")
    for i in args:
        sum = sum+i
        print(sum)
    return sum

add(10,20,30,40,50,60,70,80,90,100)

#multiple kwargs= keyword arguments

def calculate(a,b,**kwargs):
    sum =0
    print(kwargs)
    print(type(kwargs))
    print(kwargs['name'],kwargs['surname'], kwargs['age'])
    sum += a
    print("add of sum with a : ",sum)
    sum *=b
    print("mul of sum with b : ",sum)

    for key in kwargs:
        print("value is ",kwargs[key])
        print(f"key is {key}")

class Car :
    def __init__(self,**kwargs):
        self.brand = kwargs.get("brand")
        self.name = kwargs.get("name")
        self.price = kwargs.get("price")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


car = Car()
mycar = Car(brand ="nissan",name="GTR",price =2500000,color="red",seats =4)
print(mycar.seats,mycar.brand)
calculate(10,20,name ="yogesh",surname ="dhameliya",age =32)

#lable
my_label = Label(text="My Lable", font=("Helvetica",32,"bold"))
my_label.pack(side="left")
my_label.config(text="New Config Text")
my_label["text"] ="New text "
my_label["fg"] ="black"



# input or Entry

input = Entry()
input.pack(side="top")
input.config(fg="red",bg="orange")


def button_click():
    new_lable =Label()
    new_lable.pack(side="left")
    new_lable.config(text="Button got clicked",fg="black")
    input_text = input.get()
    my_label.config(text=input_text,fg="red")
#button

my_button = Button(command=button_click)
my_button.pack(side="left")
my_button.config(text="Submit",fg="red")



# It keeps window remains open
window.mainloop()