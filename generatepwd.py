import random

special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', 
                 '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?']

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers =list(range(0,10))


print("Welcome to Python Passsword Generator")
let =int(input("How many lettrs?"))
num =int(input("How many numbers?"))
sp_char =int(input("How many special characters ?"))
pwd_char =''
pwd_alpha =''
pwd_num = ''
password = []
pwd = ""
for num in range(1,num+1):
    password.append(str(random.choice(numbers)))
print(pwd_num)

for char in range(1,sp_char+1):
    password.append(random.choice(special_chars))
print(pwd_char)

for alpha in range(1,let+1):
   password.append(random.choice(alphabets))
print(pwd_alpha)

print(password)
random.shuffle(password)

for paswd in password :
    pwd += paswd

    
print(f"Your Secured Password is: {pwd}")