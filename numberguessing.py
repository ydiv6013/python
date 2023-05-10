import random

print("Welcome to the number guessing game")
print("I am thinking of number between 1 to 50")

attempt_easy = 10
attempt_hard = 5
count = 0
guess = {}

level=int(input("""Please choose your level,easy or hard
easy = 1
hard = 2 :
"""
 ))
if level == 1 :
    count = attempt_easy
    print("count is ",count)
else :
    count = attempt_hard
    print("count is ",count)



number = random.randint(1,51)

print(number)

guessed_number =int(input("Make a guess"))

if guessed_number == number :
    print(f"Welldon, number is {number}")
elif guessed_number > number  :
    print("Too high")
elif guessed_number < number :
    print("Too Low")
