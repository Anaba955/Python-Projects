import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clock_wise():
    # tim.left(10)
    # or
    angle = tim.heading() - 10
    tim.setheading(angle)


def anti_clock():
    # tim.right(10)
    # or
    angle = tim.heading() + 10
    tim.setheading(angle)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()  # listening events
screen.onkey(key="w", fun=move_forward)  # onkey() is an event listener. It calls move_forward when space is pressed
# onkey() is a higher order function that takes another function as input.
# No () at the end of move_forward when passed as input because we want move_forward to execute when space is pressed.
screen.onkey(key="s", fun=move_backward)  # use positional arguments for higher order functions
screen.onkey(key="a", fun=clock_wise)
screen.onkey(key="d", fun=anti_clock)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
