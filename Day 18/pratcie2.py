# this project is random walk of the turtle with random colors

# from turtle import Turtle, Screen,
import turtle
import random

turtle.colormode(255) # hmmmm kinda new before sa object construction i declare
timmy_the_turtle = turtle.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
    

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

direction = [0, 90, 180, 270]

while True:
    timmy_the_turtle.speed('fastest')
    timmy_the_turtle.setheading(random.choice(direction))
    timmy_the_turtle.hideturtle()
    timmy_the_turtle.width(10)
    timmy_the_turtle.forward(20)
    timmy_the_turtle.pencolor(random_color())