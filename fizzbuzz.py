print("Welcome to the python fizzbuzz game")

for number in range(1,101) :
    divide_by_3 = number % 3
    divide_by_5 = number % 5

    if  number % 3 == 0 and number % 5 == 0 :
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
         print("Buzz")
    else :
        print(number)
