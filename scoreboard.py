from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center",
                   font=("Arial", 60, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center",
                   font=("Arial", 60, "normal"))

    def score_right(self):
        self.r_score += 1
        self.update_scoreboard()
    def score_left(self):
        self.l_score += 1
        self.update_scoreboard()

