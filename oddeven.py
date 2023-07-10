
# odd or even number

number = int(input("please enter any number"))
result = number % 2
print(result)

# number % 2 if reminder is 0 then even , if reminder is 1 then odd
if result == 0 :
    print(f"Entered number {number} is even number")
else :
    print(f"Entered number {number} is odd number")

