score = input("please enter the score of the student seprated by semicolon(/)")
int_score = score.split('/')
print(max("max score using max function",int_score))
max = 0
for maxscore in int_score:
    a = int(maxscore)
    if a >= max :
        max = a

print("Max score of the student is :",max)

