print("Welcome to the Paint are calc")

width = int(input("please enter width of wall : "))
height = int(input("please enter height of wall : "))
coverage = int(input("please enter number of cans required : "))


def paintcallc(width,height,coverage):

    no_cans = (width * height) / coverage
    print(f"{round(no_cans)}  cans are required to paint the wall.")


paintcallc(width,height,coverage)