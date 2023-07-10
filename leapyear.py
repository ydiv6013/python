#Leap Year finder

year = int(input("please enter year"))

divisible_by_4 = year % 4
divisible_by_400 = year % 400
divisible_by_100 =year % 100

print(divisible_by_4,divisible_by_100,divisible_by_400)

if divisible_by_4 == 0:
   
    if divisible_by_100 == 0 :
        if divisible_by_400 == 0 :
            print(f"{year} leap year")
        else : 
            print(f"{year}Not a leap year")
    else :
        print(f"{year}leap year")
else :
    print(f"{year}Not a leap year")