import random as rand
#

name = input("Please Enter a person name seperated by comma(,) : ")
name_list = name.split(',')
person_length = len(name_list)
print(name_list , person_length)
random = rand.randint(0,person_length - 1)
print(random)

print(f"Hey, {name_list[random]} is lucky person, {name_list[random]} will pay the bill")
