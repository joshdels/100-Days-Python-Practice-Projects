import colorgram
import random
import turtle as t

colors = colorgram.extract(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 18\hirst\image.jpg", 15)

def random_color():
    '''returns a tuple of rgb for colors'''
    random_choice = random.randint(0 , len(colors))
    r, g, b = colors[random_choice-1].rgb
    return r, g, b

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.penup()

def dot():
    '''creates dot on the screen with random color'''
    tim.penup()
    tim.dot(20, random_color())
    tim.speed('slow')

X = -300
Y = -280

for n in range(10):
    tim.setposition(X, Y)
    for i in range(10):
        dot()
        tim.forward(50)
    Y += 50
    
#done chef kiss




















screen = t.Screen()
screen.exitonclick()