from turtle import Turtle
import random
SPEED = 2
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
            if self.xcor() > 400 or self.xcor() < -400:
                print("Game Over")
                self.reset()
                ball_is_fowarding = False
            else:
                self.forward(10)
                if self.detect_wall():
                    self.bounce_vertical()
                
    def detect_wall(self):
        if self.ycor() > 300 or self.ycor() < -300:
            print("hit top or bottom")
            return True
        return False
    
    # def detech_paddle(self, paddle1, paddle2):
    #     if self.pos() == self.paddle1.pos() or self.pos() == self.paddle2:
    #         pass
            
    def bounce_vertical(self):
        if self.detect_wall():
            new_heading = -self.heading()
            self.setheading(new_heading)
            
    def bounce_paddle(self):
        current_heading = self.heading()
        new_heading = 180 - current_heading()
        self.setheading(new_heading)
        
    def reset(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
