
old_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_list = []
name = "Yogesh"
letters = []
for n in old_list:
    add_new = n+1
    new_list.append(add_new)

print(new_list)

# same using list comprehension

new_list = [n+1 for n in old_list]

print(new_list)
name_list = [n for n in name]

print(name_list)

double_list =[n*2 for n in range(1,5)]

print(double_list)

# conditional comprehension

countries = [ "Finland","Norway","Denmark","Iceland","Switzerland"]
new_country = [country for country in countries if len(country) > 7 ]

print(new_country)

new_country_upper = [country.upper() for country in countries if len(country) > 7 ]

print(new_country_upper)

squared_num_list = [num*num for num in old_list]

print(squared_num_list)

even_number = [num for num in old_list if num % 2 == 0]
odd_number =[num for num in old_list if num % 2 != 0]
print(even_number)
print(odd_number)

result = [ num for num in squared_num_list if num in even_number]

print(result)