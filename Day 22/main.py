from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

# Agenda
#TODO 1 Create the screen
screen = Screen()
screen.title("My Pong Game")
screen.bgcolor("black")
screen.setup(height=600, width=800)

#TODO 3 Create another paddle
paddle1 = Paddle(-390, 0)
paddle2 = Paddle(390, 0)

#TODO 4 Create athe ball and make it move
ball = Ball()
ball.move_ball()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")





#TODO 5 Detect collision with wall and bounce
#TODO 6 Detect collision with paddle
#TODO 7 Detect when paddle misses
#TODO 8 Keep Score






# my solution
# Create 2 players paddle
    # Move up and down

# create Middle Net
    # Ball will respawn here

# Create Ball 
    # Ball will move randomly in left to right 
    # Ball will bounce in each paddle

# create Scoreboard


screen.exitonclick()