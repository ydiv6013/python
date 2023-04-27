
# pizza order calculation S= small pizza, M = medium pizza , L = Large Pizza

s = 15
m = 20
l = 25
pep = 2
che = 3
price = 0
print("Welcom to the python Pizza")
size = input("Please Enter Size of Pizza i.e S for small , M for medium , L for Large")
print (size)
if size == 'S' :
    price = s
elif size == 'M':
    price = m
else :
    price = l
print(price)
peproni = input("Want peproni ? (Y/N) ")
if peproni == 'Y' :
    price = price + pep
else :
    price = price
print(price)
cheese = input ("Extra Cheese ? (Y/N)")
if cheese == 'Y' :
    price = price + che
else :
    price = price
print(price)

print(f"Your Final bill is :{price}$ ")