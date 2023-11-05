from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


def setup_screen(main_screen, left_paddle, right_paddle):
    main_screen.bgcolor("black")
    main_screen.setup(800, 600)
    main_screen.title("Pong Game")
    main_screen.tracer(0)
    main_screen.listen()
    main_screen.onkeypress(right_paddle.go_up, "Up")
    main_screen.onkeypress(right_paddle.go_down, "Down")
    main_screen.onkeypress(left_paddle.go_up, "w")
    main_screen.onkeypress(left_paddle.go_down, "s")


def run():
    screen = Screen()
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    setup_screen(screen, l_paddle, r_paddle)
    ball = Ball()
    scoreboard = Scoreboard()

    game_is_on = True

    screen_divider = Turtle("square")
    screen_divider.color("white")
    screen_divider.penup()
    screen_divider.goto(0, 295)
    screen_divider.setheading(270)
    screen_divider.pendown()
    screen_divider.pensize(5)

    for _ in range(15):
        screen_divider.forward(20)
        screen_divider.penup()
        screen_divider.forward(20)
        screen_divider.pendown()


    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Right paddle miss
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.left_add_point()

        # Left paddle miss
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.right_add_point()

    screen.exitonclick()


run()
