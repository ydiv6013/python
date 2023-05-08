
#function with no parameter
def greet() :
    print("Hello")
    print("How are you")
  

#function with one parameter
def person(name):
    print(f"name is {name}")
#function with multiple parameter

def person_age(name,age):
    return(f"name is {name} and age is {age}")
    print("this will be never printed as return statement ends the function")



def func_return(name,age) :
    #docstring
    """please enter the name and age ,name must be in string and age in integer"""
    if name == "" :
        return "Please enter name "
    elif age == "":
        return "please enter age"
    else :
        return(f"name is {name} and age is {age}")

name = input("Please enter your name :" ).title()
age = int(input("please enter your age : "))


#function call with no argument
greet()
#function call with one argument
person(name)
#function call with multiple argument
func_return =func_return(input("name"),input("age"))
print(func_return)
person_age(age=age,name=name)

