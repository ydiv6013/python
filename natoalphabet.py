import pandas as pd

filehandler = open("files/nato_phonetic_alphabet.csv")

data = pd.read_csv(filehandler)
print(data)

for (key , value) in data.items():
    print(key)

for (index,row) in data.iterrows():
    print(index)
    print(row)
    print(row.letter)
    print(row.code)

# dictionary comprehension
alpha_dictionary ={row.letter : row.code for (index,row) in data.iterrows()}

print(alpha_dictionary)

data2 = pd.Series(alpha_dictionary)

print(data2)
print(pd.Series(len(alpha_dictionary)))
'''
# create a dictionary using pandas
print("using pandas\n", data.to_dict())

name =input("Please enter your name : ").upper()
print([alpha_dictionary[letter] for letter in name])
'''