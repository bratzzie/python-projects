from turtle import Turtle

SCORE_FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.redisplay_scores()

    def redisplay_scores(self):
        self.clear()

        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=SCORE_FONT)

        self.goto(100, 200)
        self.write(self.right_score, align="center", font=SCORE_FONT)

    def left_add_point(self):
        self.left_score += 1
        self.redisplay_scores()

    def right_add_point(self):
        self.right_score += 1
        self.redisplay_scores()
