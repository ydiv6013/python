import random

print("Welcome to the Python Hangman Game")

#word = ["mango","apple","grapes","orange","cherry"]s
 
word = ["cherry"]
selected_word = random.choice(word)
word_length = len(selected_word)
guassed_word =[]
life = word_length
for i in range(1,word_length+1):
    guassed_word.append("_")
print(guassed_word,selected_word)

print(f"computer has selected {word_length} length word to guess and save a man to be hanged\n")
print(f"wrong letter will decrease the life of man, life is {life}")

for i in range(1,word_length+1):
    inputed_word = input("please enter one letter to continue game: \n").lower()
    print(f"you have entered {inputed_word}" )
    count =selected_word.count(inputed_word)
    print(f"we find {count} :{inputed_word} ")
    pos =selected_word.find(inputed_word)
    print(f"position of the entered word is {pos}")

    for i in selected_word :

        if inputed_word == i :
            print("great, your word mateched\n")
            if count > 1 :
                new_pos = int(input("please enter a  word position to fill: "))-1
                guassed_word.pop(new_pos)
                guassed_word.insert(new_pos,inputed_word)
                print(guassed_word)
                break
            else :
                guassed_word.pop(pos)
                guassed_word.insert(pos,inputed_word)
                print(guassed_word)
        else :
            print("oops,word not matched")
            life = life -1
            print(f"life is {life}")
            break
       # print("selected word is",j)

for j in inputed_word :
        if j in selected_word :
            print("great, your word mateched\n",j)
            guassed_word.insert(pos,inputed_word)
            guassed_word.pop(pos+1)
            print(guassed_word)
        
        else :
            print("oops",j,life)
            life = life -1
            print(f"life is {life}")
       # print("selected word is",j)
    
