from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

color_range = ['red', 'yellow', 'blue', 'pink', 'green', 'dark sea green', 'orange']

# square

# num = 0
# condition = True
# while condition:
#     if num <10:
#         print(f"ok {num}")
#         num += 1
#     else:
#         condition = False
    
# num = 0
# condition = True
# while condition:
#     angle = 360 / (num + 2) 
#     for n in range(num + 2):
#         random_color = random.choice(color_range)
#         timmy_the_turtle.speed(3)
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#     timmy_the_turtle.color(random_color)
#     num += 1


# draw dashed line
# for i in range(15):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(5)


# num = 0
# for num in range(2 + num):
#     angle = int(360/(2 + num))
#     #turtle angle
#     timmy_the_turtle.right(angle)
#     timmy_the_turtle.forward(50)
#     num =+ 1

# random walk
direction = [0, 90, 180, 270]

while True:
    timmy_the_turtle.speed('fastest')
    timmy_the_turtle.setheading(random.choice(direction))
    timmy_the_turtle.hideturtle()
    timmy_the_turtle.width(10)
    timmy_the_turtle.forward(20)
    timmy_the_turtle.color(random.choice(color_range))



    












screen = Screen()
screen.exitonclick()