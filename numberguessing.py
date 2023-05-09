import random


number = random.randint(0,1)

print("Welcome to the number guessing game")
print("I am thinking of number between 1 to 50")
level=int(input("""Please choose your level,easy or hard
easy = 1
hard = 2 :
"""
 ))

attempt_easy = 10
attempt_hard = 5


number = random.randint(1,51)

print(number)

guessed_number =int(input("Make a guess"))

if guessed_number == number :
    print(f"Welldon, number is {number}")
elif guessed_number > number  :
    print("Too high")
elif guessed_number < number :
    print("Too Low")
