from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=3, stretch_len=0.5,)
        self.speed("fastest")
        self.goto(x,y)
        
    #TODO 2 Create and move a paddle
    def up(self):
        self.goto(self.xcor(), self.ycor() + 40)
        
    def down(self):
        self.goto(self.xcor(), self.ycor() +-40)
        
        