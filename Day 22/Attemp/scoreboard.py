from turtle import Turtle
FONT = ['Courier', 15, 'normal']

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('White')
        self.penup()
        self.hideturtle()
        self.SCORE1 = 0
        self.SCORE2 = 0
        self.goto(0, 260)
        self.update_score()

        
    def update_score(self):
        self.clear()
        self.write(f"{self.SCORE2} | SCORE | {self.SCORE1}", align='center',font=FONT)
    
    def game_over(self):
        self.color('White')
        self.hideturtle()
        self.write("Game Over", align='center', font=FONT)