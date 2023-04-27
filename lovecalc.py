
print("Welcome to the love calculator")

name1 = input("Enter your name : ").lower()
name2 = input("Enter your partner's name : ").lower()

name = name1 + name2
print(name1,name2)
T = name.count('t')
R = name.count('r')
U = name.count('u')
E = name.count('e')

true = T + R + U + E

print("TRUE Score is " ,true)
l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')


love = l + o + v + e
print("LOVE Score is " ,love)
print(l,o,v,e,love)

total = true + love
if  total < 10 or total > 90 :
    print(f"Your Score is {total},you both are True Lover")
elif total > 40 and total < 50 :
    print(f"Your Score is {total},you go alright togather")
else :
    print(f"Your Score is {total}.")
