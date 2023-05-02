
#function with no parameter
def greet() :
    print("Hello")
    print("How are you")
  

#function with one parameter
def person(name):
    print(f"name is {name}")
#function with multiple parameter

def person_age(name,age):
    print(f"name is {name} and age is {age}")

name = input("Please enter your name :" )
age = int(input("please enter your age : "))


#function call with no argument
greet()
#function call with one argument
person(name)
#function call with multiple argument
person_age(name,age)
person_age(age=age,name=name)
