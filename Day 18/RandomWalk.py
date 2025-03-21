# this project is random walk of the turtle with random colors

from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

color_range = ['red', 'yellow', 'blue', 'pink', 'green', 'dark sea green', 'orange']

direction = [0, 90, 180, 270]

while True:
    timmy_the_turtle.speed('fastest')
    timmy_the_turtle.setheading(random.choice(direction))
    timmy_the_turtle.hideturtle()
    timmy_the_turtle.width(10)
    timmy_the_turtle.forward(20)
    timmy_the_turtle.color(random.choice(color_range))