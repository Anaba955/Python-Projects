import colorgram  # extract colors from image
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

# colors = colorgram.extract('dots.jpeg', 25)
# list_of_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     list_of_colors.append((r, g, b))
#
# print(list_of_colors)

color_list = [(189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (83, 133, 108),
              (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89),
              (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88),
              (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181)]

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

no_of_dots = 100
for dot_count in range(1, no_of_dots + 1):
    tim.color(random.choice(color_list))
    tim.dot(20)
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
