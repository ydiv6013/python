print( """
 ______       ________       __           ______       __  __       __           ________       _________   ______       ______       
/_____/\     /_______/\     /_/\         /_____/\     /_/\/_/\     /_/\         /_______/\     /________/\ /_____/\     /_____/\      
\:::__\/     \::: _  \ \    \:\ \        \:::__\/     \:\ \:\ \    \:\ \        \::: _  \ \    \__.::.__\/ \:::_ \ \    \:::_ \ \     
 \:\ \  __    \::(_)  \ \    \:\ \        \:\ \  __    \:\ \:\ \    \:\ \        \::(_)  \ \      \::\ \    \:\ \ \ \    \:(_) ) )_   
  \:\ \/_/\    \:: __  \ \    \:\ \____    \:\ \/_/\    \:\ \:\ \    \:\ \____    \:: __  \ \      \::\ \    \:\ \ \ \    \: __ `\ \  
   \:\_\ \ \    \:.\ \  \ \    \:\/___/\    \:\_\ \ \    \:\_\:\ \    \:\/___/\    \:.\ \  \ \      \::\ \    \:\_\ \ \    \ \ `\ \ \ 
    \_____\/     \__\/\__\/     \_____\/     \_____\/     \_____\/     \_____\/     \__\/\__\/       \__\/     \_____\/     \_\/ \_\/ 
                                                                                                                                      

"""
)

#add
def addition(num1,num2):
    """Please add two number and can not be string"""
    
    result = num1 + num2
    return f"{num1} + {num2} = {result}"


def subtraction(num1,num2):
    """Please add two number and can not be string"""

    result = num1 - num2
    return f"{num1} - {num2} = {result}"

def multipliocation(num1,num2):
    """Please add two number and can not be string"""

    result = num1 * num2
    return f"{num1} * {num2} = {result}"

def division(num1,num2):
    """Please add two number and can not be string"""

    result = num1 / num2
    return f"{num1} / {num2} = {result}"


operations ={
    "+" : addition , 
    "-" : subtraction ,
    "*" : multipliocation,
    "/" : division
}
value1 = float(input("please enter num 1 : "))
value2 = float(input("please enter num 2 : "))
next = True


for symbol in operations:
    print(symbol)
option = input("please enter any options as above : ")


if option == "+" :
   operations["+"]
   print(addition(value1,value2))

elif option == "-" :
    operations["-"]
    print(subtraction(value1,value2))
elif option == "*" :
    operations["*"]
    print(multipliocation(value1,value2))
elif option == "/" :
    operations["/"]
    print(division(value1,value2))
else :
    print("you have entered wrong input please.try again")

while next:
    choice =input("Want to continue ? y or n")

    if choice == "y" :
        print(next)
    else :
        next = False
        print("Thanks")
        print(next)