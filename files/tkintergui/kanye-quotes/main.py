from tkinter import *
import urllib.request ,urllib.error ,urllib.parse
import json
import certifi

def get_quote():
        
    api_endpoint ="https://catfact.ninja/fact"

    urlhandler = urllib.request.urlopen(api_endpoint,cafile=certifi.where())
    print(urlhandler)
    data = urlhandler.read()
    print(type(data))
    try :
        js = json.loads(data)
    except :
        js = None

    print(type(js))
    if not js or 'status' not in js or js['status'] != 'OK' :
        print("something went wrong")

    data_js = json.dumps(js,indent=4)
    fact =js['fact']
    canvas.itemconfig(quote_text,text=fact)
    print(type(data_js))
    print(data_js)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="files/tkintergui/kanye-quotes/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="files/tkintergui/kanye-quotes/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()