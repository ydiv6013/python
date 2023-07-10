from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("files/tkintergui/flash-card/data/french_words.csv")
to_learn = data.to_dict(orient ="records")
current_card ={}

def next() :
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card["English"])
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_image,image=image_url)
    flip_timer=window.after(3000,func=flip)
    
    

def flip():
    canvas.itemconfig(card_image,image=flip_image_url)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    print("flip works")
    


window = Tk()

window.title("Flash Card App")
window.config(padx=20,pady=20,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip)


canvas = Canvas()
canvas.config(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
flip_image_url = PhotoImage(file="files/tkintergui/flash-card/images/card_back.png")
image_url = PhotoImage(file="files/tkintergui/flash-card/images/card_front.png")
card_image=canvas.create_image(800/2,526/2,image=image_url)
card_title=canvas.create_text(400,160,text="Title",font=("Helvetica",40,"italic"),fill="black")
card_word=canvas.create_text(400,260,text="word",font=("Helvetica",60,"bold"),fill="black")
canvas.grid(column=0,row=0,columnspan=2)

cross_img = PhotoImage(file="files/tkintergui/flash-card/images/wrong.png")
right_img = PhotoImage(file="files/tkintergui/flash-card/images/right.png")

cross_btn = Button()
cross_btn.config(image=cross_img,command=next,highlightthickness=0,
                 highlightbackground=BACKGROUND_COLOR,bg=BACKGROUND_COLOR)
cross_btn.grid(column=0,row=1)


right_btn = Button()
right_btn.config(image=right_img,command=next,highlightthickness=0,
                 highlightbackground=BACKGROUND_COLOR,bg=BACKGROUND_COLOR)
right_btn.grid(column=1,row=1)


next()
window.mainloop()