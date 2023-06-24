from tkinter import *

THEME_COLOR = "#375362"

def true():
    pass

def wrong():
    pass

class QuizInterface :
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizller")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_lbl = Label()
        self.score_lbl.config(text="Score : 0",fg="white" ,bg=THEME_COLOR)
        self.score_lbl.grid(column=1,row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300,height=250,bg="white")
        self.que=self.canvas.create_text(150,125,
                                         text="Question",
                                         font=("Helvetica",20,"italic"),
                                         fill="black")
        self.canvas.grid(column=0,row=1,columnspan=2,pady=20)


        self.true_img = PhotoImage(file="files/tkintergui/Quizzler/images/true.png")
        self.false_img = PhotoImage(file="files/tkintergui/Quizzler/images/false.png")
        
        self.false = Button()
        self.false.config(image=self.false_img,command=wrong,highlightthickness=0,
                 highlightbackground=THEME_COLOR,bg=THEME_COLOR)
        self.false.grid(column=0,row=2,pady=20)

        self.true = Button()
        self.true.config(image=self.true_img,command=true,highlightthickness=0,
                 highlightbackground=THEME_COLOR,bg=THEME_COLOR)
        self.true.grid(column=1,row=2,pady=20)

       


        self.window.mainloop()