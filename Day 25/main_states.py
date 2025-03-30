import os
import turtle
import pandas

FONT = ['Arial', 8, 'normal']
path = os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 25")

correct_states = []

screen = turtle.Screen()
screen.title("U.S. Sates Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def create_location(x,y, state):
    '''This will move the state into the map'''
    location = turtle.Turtle()
    location.hideturtle()
    location.penup()
    location.goto(int(x),int(y))
    location.write(state, align='center', font=FONT)

data = pandas.read_csv("50_states.csv")

game_is_on = True
while game_is_on: 
    
    # add scores
    score = len(correct_states)
    total_items = len(data)
    
    # this will prompt the user to take a guess
    answer_state = screen.textinput(title=f"Guess the State {score}/{total_items}", prompt="What's another state's name?")
    my_answer = answer_state.title()
    
    #this will check if the answe if right, if not it will go again
    guessed_state = data[data["state"] == my_answer]
    
    if not guessed_state.empty:
        correct_states.append(my_answer)
        x = guessed_state.iloc[0]['x']
        y = guessed_state.iloc[0]['y']

        create_location(x,y,my_answer)
        
        
    else:
        print("Wrong answer")
        
    






screen.exitonclick()



# REFLECTION
# what i've learned is that i should create another instance object if i want to use the same specific method of an object to avoid objects property usage

