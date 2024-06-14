from turtle import Turtle
import random


class Food(Turtle):  # inheriting Turtle class instead of creating an object in food class.
    # Food class now has all props of Turtle class

    def __init__(self):
        super().__init__()  # initialize food class with all Turtle class attributes and methods
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)  # a turtle object has 20 20 size and to get 10 we divide by half
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
