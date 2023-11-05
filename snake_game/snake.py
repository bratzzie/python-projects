from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP_MOVE_DISTANCE = 20
HEADING_UP = 90
HEADING_DOWN = 270
HEADING_LEFT = 180
HEADING_RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_index - 1].xcor()
            new_y = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(new_x, new_y)
        self.head.forward(STEP_MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != HEADING_DOWN:
            self.head.setheading(HEADING_UP)

    def move_down(self):
        if self.head.heading() != HEADING_UP:
            self.head.setheading(HEADING_DOWN)

    def move_left(self):
        if self.head.heading() != HEADING_RIGHT:
            self.head.setheading(HEADING_LEFT)

    def move_right(self):
        if self.head.heading() != HEADING_LEFT:
            self.head.setheading(HEADING_RIGHT)
