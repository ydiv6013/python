print("welcome to the pythons ceaser cipher encryption")

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

en_type= input("Type 'e' for encrypt and 'd' for decryption :").lower()
cipher = int(input("please enter cipher : "))
msg = input("Enter your message : ").lower()
en_msg =[]
de_msg =[]

def encryption(msg,cipher) :
    en_text =""
    for letter in msg :
        pos = alphabets.index(letter)
        new_index = pos + cipher
        replaced_alpha = alphabets[new_index]
        en_msg.append(replaced_alpha)

    for en_letters in en_msg :
        en_text += en_letters
    print("Encrypted text is :" , en_text)

def decryption(msg,cipher):
    decoded_text=""
    decoded_list =[]
    for de_letters in msg :
        de_msg.append(de_letters)
        position = alphabets.index(de_letters)
        new_position = position - cipher
        replaced_alpha =alphabets[new_position]
        decoded_list.append(replaced_alpha)
    
    for alpha in decoded_list :
        decoded_text += alpha
        
    print("Decrypted text is ",decoded_text)

if en_type == 'e':
    encryption(msg,cipher)
else :
    decryption(msg,cipher)