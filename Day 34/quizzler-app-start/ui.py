from tkinter import *
from quiz_brain import QuizBrain
import os
os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 34\quizzler-app-start")

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window =  Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="text", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2,padx=20, pady=20)
        
        # button
        self.true_image = PhotoImage(file=r"images\true.png")
        self.false_image = PhotoImage(file=r"images\false.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column=0,row=2, padx=20, pady=20)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(column=1,row=2, padx=20, pady=20)
        
        # score
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "normal"))
        self.score.grid(column=1, row=0, padx=20, pady=20) 
        
    
        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reach to the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))
 
    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right):
 
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, func=self.get_next_question)
        
  
        



