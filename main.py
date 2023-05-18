#creating an empty class

class Car:
    pass


car =Car()
car.color ="red"
car.type = "EV"

print(car.color,car.type)


#creating an constructor with no attributes

class NewCar :
    def __init__(self) -> None:
        print("Creating an constructor")

#creating an constructor with one attributes

class BigCar:
    def __init__(self,seat):
        self.noofseat = seat

#creating an constructor with multiple attributes

class User:
    #creating a constructor
    def __init__(self,user_id,user_name,age):
        self.userid = user_id
        self.username = user_name
        self.age = age

    def login(self,xyz):
        self.userid ="yogesh rameshbhai dhameliya"
        print("login methods")

newcar =NewCar()
#print(newcar)

bigcar =BigCar(seat = int(input("Please enter no of seats : ")))
print(bigcar.noofseat)

u_name =input("Please enter username : ")
u_id = input("please enter user id : ")
u_age =input("please enter ade : ")


user =User(u_id,u_name,u_age)
print(f"name of the user is {user.username} id is {user.userid} & age is {user.age}")
user.login("abc")
print(f"{user.userid}")
