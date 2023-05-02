print("Welcome to the python's prime number finder")

num = int(input("plesase enter number to check wheather it's prime or not : "))

def prime(num):
    is_prime = True
    for i in range(2,num):
        if (num % i) == 0:
            is_prime = False
    if is_prime :
        print(f"Entered number {num} is prime number")
    else :
         print(f"Entered number {num} is not a prime number")

prime(num)