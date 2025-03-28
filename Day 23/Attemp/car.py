from turtle import Turtle
import random
COLORS = ['red', 'blue', 'black', 'orange']

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.showturtle()
        self.generate_cars()
        # self.move()
        
    def generate_cars(self):
        for color in COLORS:
            y_coor = random.randint(-250, 300)
            self.hideturtle()
            self.color(color)
            self.goto(350, y_coor) 
            self.showturtle()
        self.move()
        
    def move(self):
        self.forward(1000)
        
    def reset_cars(self):
        self.hideturtle()
        self.goto(350,0)
        self.showturtle()
        self.move()