

# Ticket counter

height = int(input("What is your Height?"))

print(" Height is",height)

if height >= 120 :
    print("Yay ! You are allowed to ride rollercoaster")
    age = int(input("What is your age?"))
    charge1 =12
    charge2 = 7
    charge3 = 5

    if age > 18 :
        print(f"Please pay {charge1}$ to ride")
    elif age > 12 :
        print(f"Please pay {charge2}$ to ride")
    else :
        print(f"Please pay {charge3}$ to ride")
else :
    print("Sorry ! You are not allowed to ride rollercoaster")