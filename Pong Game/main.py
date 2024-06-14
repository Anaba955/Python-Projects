from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# center line
line = Turtle()
line.penup()
line.color("white")
line.shape("square")
line.hideturtle()
line.goto(0, -300)
line.setheading(90)

while line.ycor() < 300:
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision on top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        ball.move_speed *= 0.9  # increase speed

    if ball.xcor() > 370:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -370:
        score.r_point()
        ball.move_speed = .1
        ball.reset_position()


screen.exitonclick()
