from turtle import Turtle, Screen
from player import Player
from car import Car 
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("My Turtle Crossing")
# screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car = Car()


screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
        
    #detech collision 
    if player.ycor() > car.ycor():
        print("hit!")
        # player.reset()
    
    # reach finish line
    if player.ycor() > 100:
        player.reset()
        scoreboard.LEVEL += 1
        scoreboard.update_scoreboard()
        



screen.exitonclick()

# REALIZATION
# 1. did not break down the problem throughly
# 2. attmep was good, but the creation of cars did not create a car list
# 3. also collision bit confuse but, it is what it is brooo