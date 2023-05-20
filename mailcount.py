email_id = ""
try :
    fhand = open("mbox.txt")
except:
    print("file not found")

def setEmail(email):
    try:
        with open("email.txt", "a") as file :
            file.write(email)
    except:
        print("File not found")

for line in fhand :
    if line.startswith('From '):
        data = line.split()
        email = data[1] + "\n"
        setEmail(email)
       

fhand.close()