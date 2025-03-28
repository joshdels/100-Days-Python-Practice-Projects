from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((-350,0))
l_paddle = Paddle((350,0))

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()
        
    #detech collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
        
    # r_side
    if ball.xcor() >400:
        ball.reset()
        scoreboard.l_point()
        
    # l_side
    if ball.xcor() < -400:
        ball.reset()
        



screen.exitonclick()