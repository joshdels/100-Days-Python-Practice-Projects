# it turns circleeee whahah

import turtle as t
import random

t.colormode(255) # hmmmm kinda new before sa object construction i declare
tim = t.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

n = 0
while True:
    tim.speed('fastest')
    tim.circle(80)
    tim.pencolor(random_color())
    tim.setheading(n)
    n += 5
    
screen = t.Screen()
screen.exitonclick()