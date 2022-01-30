from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    collided = False
    fps = 0.1
    time.sleep(fps)
    ball.move()
    screen.update()

    if ball.ycor()>280 or ball.ycor() <-280:
        #needs to bounce
        ball.bounce(x=1,y=-1)

    #detect coll with  paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle)< 50 and ball.xcor() < -320:
        ball.bounce(x=-1, y=1)

        fps/= 20
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        fps = 0.1
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        fps = 0.1


screen.exitonclick()
