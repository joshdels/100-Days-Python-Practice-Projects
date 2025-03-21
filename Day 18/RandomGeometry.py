# random shape generator with random color selector

from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

color_range = ['red', 'yellow', 'blue', 'pink', 'green', 'dark sea green', 'orange']

num = 0
condition = True
while condition:
    angle = 360 / (num + 2) 
    for n in range(num + 2):
        random_color = random.choice(color_range)
        timmy_the_turtle.speed(3)
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)
    timmy_the_turtle.color(random_color)
    num += 1
    
screen = Screen()
screen.exitonclick()