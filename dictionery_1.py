
print("Dictionary Basics")

dictionary = {"name" :"yogesh","surname" :"dhameliya"}

print(dictionary)
print(f"name is : {dictionary['name']}\nsurname is : {dictionary['surname']}")

# adding a new key value pair to dictionary

dictionary["age"] = 32

print(dictionary)
print(f"Name is : {dictionary['name']}\nSurname is : {dictionary['surname']}\nAge is : {dictionary['age']} ")



#edit an item in a Dictionary

dictionary["name"] =""
print(dictionary)


dictionary["name"] ="Hiren"
dictionary["age"] = 30
print(dictionary)


#loop through a dictionary
for key in dictionary:
    print(key)
    print(dictionary[key])



#create or empty all data from dictionary

dictionary ={}

print(dictionary)