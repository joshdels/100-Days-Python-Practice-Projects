import os
os.chdir("C:/Users/deleo/OneDrive/Documents/GitHub/100-Days-Python-Practice-Projects/Day 20")
from turtle import Turtle



ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}" , align=ALIGNMENT, font=FONT) 
     
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)   
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{(self.high_score)}")
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard() 
        