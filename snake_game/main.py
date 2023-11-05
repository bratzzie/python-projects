from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def init_main_screen(main_screen):
    main_screen.setup(600, 600)
    main_screen.bgcolor("black")
    main_screen.title("Snake Game")
    main_screen.tracer(0)

    main_screen.listen()
    main_screen.onkey(snake.move_up, "Up")
    main_screen.onkey(snake.move_down, "Down")
    main_screen.onkey(snake.move_left, "Left")
    main_screen.onkey(snake.move_right, "Right")


def run():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move_snake()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.gave_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.gave_over()

    screen.exitonclick()


screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
init_main_screen(screen)
run()
