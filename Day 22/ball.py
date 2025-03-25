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
        self.setheading(random.randint(1,360))        
    
    def move_ball(self):
        ball_is_fowarding = True
        while ball_is_fowarding:
            self.forward(10)
            if self.detect_wall():
                self.bounce()
                ball_is_fowarding = False
            
    def detect_wall(self):
        if self.xcor() > 300 or self.xcor() < -300:
            print("hit left or right")
            return "horizontal"
        if self.ycor() > 400 or self.ycor() < -400:
            print("hit top or bottom")
            return "vertical"
        return None

    def bounce(self):
        wall = self.detect_wall()
        if wall == "horizontal":
            new_heading = 180 - self.heading()
        elif wall == "vertical":
            new_heading = -self.heading()
        self.setheading(new_heading)
