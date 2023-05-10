import random

print("Welcome to the number guessing game")
print("I am thinking of number between 1 to 50")

attempt_easy = 10
attempt_hard = 5
count = 0
guess = {
    "guessed_number": '',
}
next = True

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

while next :
    print("next is ", next)
    if count > 0:
        guessed_number =int(input("Make a guess"))
        if guessed_number == number :
            print(f"Welldon, number is {number}")
            guess["guessed_number"] = guessed_number
            next = False
        elif guessed_number > number  :
            print("Too high")
            guess["guessed_number"] = guessed_number
            count = count - 1
            print("count is " , count)
        elif guessed_number < number :
            print("Too Low")
            guess["guessed_number"] = guessed_number
            count = count - 1
            print("count is " , count)
    else :
        print("No count left ,Betterluck nexttime!")

print(count)
print(guess)