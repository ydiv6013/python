
#KeyError

person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "email": "johndoe@example.com"
}

try :
    key = input("Please enter key from person dictionary : ")
    print(person[key])
except KeyError as error:
    print(f"{error}")
else :
    print([key for key in person])
finally :
    print("Error handling")

exit()
#IndexError

fruites =["apple","Banana","Orange"]

try :
    index = int(input("Please enter index to get value from fruites list : "))
    print(fruites[index])
except IndexError as error:
    print(f"{error}")
else :
    print([fruite for fruite in fruites])
finally :
    print("Error handling")
