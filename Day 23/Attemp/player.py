from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.setheading(90)
        self.penup()
        self.goto(0,-280)
        self.showturtle()
        
    def move_up(self):
        self.forward(20)
        
    def move_down(self):
        self.backward(10)
        
    def reset(self):
        self.hideturtle()
        self.goto(0,-280)
        self.showturtle()
        
        

        

    