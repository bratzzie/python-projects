from turtle import Turtle

STEP_MOVE = 20


class Paddle(Turtle):
    def __init__(self, init_coords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(init_coords)

    def go_up(self):
        new_y = self.ycor() + STEP_MOVE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - STEP_MOVE
        self.goto(self.xcor(), new_y)
