from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_paddle = 0
        self.r_paddle = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_paddle, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_paddle, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_paddle += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_paddle += 1
        self.update_scoreboard()
