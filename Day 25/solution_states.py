import os
import turtle
import pandas

path = os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 25")


screen = turtle.Screen()
screen.title("U.S. Sates Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


guessed_states = []
# left_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        #leaning curve of missing states
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item())) #.item() for panda series
        t.write(answer_state)
    
    
# #states_to_learn.csv attemp to solve and create a csv for missing states
# for correct_guess in guessed_states:
#     remaining_states = data[data.state != correct_guess]
#     left_states.append(remaining_states)

# dict_data = {
#     "States": left_states
# }
# new_data = pandas.DataFrame(dict_data)
# new_data.to_csv("reamaining_states.csv")


screen.exitonclick()