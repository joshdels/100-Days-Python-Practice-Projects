from turtle import Turtle
import random
SPEED = 10
X_COOR = 0
Y_COOR = 0

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.speed(SPEED)
        
    def move_ball(self):
        random_heading = random.randint(1, 360)
        self.setheading(random_heading)
        for i in range(100):
            self.forward(10)
