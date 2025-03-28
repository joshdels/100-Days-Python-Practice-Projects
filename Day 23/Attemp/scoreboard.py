from turtle import Turtle
FONT = ['Arial', 12, 'normal']
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.LEVEL = 1
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(f'Level {self.LEVEL}', align='center', font=FONT)
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'Level {self.LEVEL}', align='center', font=FONT)
        