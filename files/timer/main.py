from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
clock = None

# ------------------------- Window ------------------------------------#
window = Tk()
#Set the geometry of tkinter frame
window.geometry("500x600")
window.title("Pomodoro")
window.config(padx=50,pady=50,bg=YELLOW)


    
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countDown(count):
    global clock
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count > 0 :
        canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
        clock = window.after(1000,countDown,count-1)

def timerStart():
    countDown(25*60)
    

def timerReset():
    window.after_cancel(clock)
    canvas.itemconfig(timer_text,text = "00:00")
    
# ---------------------------- UI SETUP ------------------------------- #

timer = Label()
timer.config(text="Timer", font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
timer.grid(column=2,row=1)

canvas =Canvas(width=250,height=250,bg=YELLOW,highlightthickness=0)
image_url = PhotoImage(file="files/timer/tomato.png")
canvas.create_image(120,100,image = image_url)
timer_text = canvas.create_text(125,125,text="00:00", font=(FONT_NAME,38,"bold"),fill="white")
canvas.grid(column=2,row=2)
 
start = Button()
start.config(text="Start", command=timerStart,fg="black",highlightthickness=0,highlightbackground=YELLOW)
start.grid(column=1,row=3)

reset = Button()
reset.config(text="Reset", command=timerReset,fg="black",highlightthickness=0,highlightbackground=YELLOW)
reset.grid(column=3,row=3)

window.mainloop()