
height = input("please enter height of the student seprated by semicolon(;)")
heights = height.split(';')
avg = 0
for avgheight in heights:
    avg += int(avgheight)
print(heights)
print("Average Height of the student is :",avg)

