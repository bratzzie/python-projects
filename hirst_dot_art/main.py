import colorgram
import turtle as t
from random import choice


SPACE_SIZE = 50
DOT_SIZE = 25


def extract_colors(image_name, number_of_colors, ):
    colors = colorgram.extract('spot_art.jpg', 25)
    colors_list = []

    for color in colors:
        color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
        colors_list.append(color_tuple)

    return colors_list


def start_new_line(turtle):
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)


def draw_spot_painting(image_of_colours, number_of_colors, number_of_spots):
    screen = t.Screen()
    screen.setup(600, 600)
    turtle = t.Turtle()

    t.colormode(255)
    turtle.speed("fastest")
    turtle.penup()
    turtle.hideturtle()

    turtle.setheading(225)
    turtle.forward(325)
    turtle.setheading(0)

    color_tuples = extract_colors(image_of_colours, number_of_colors)

    for i in range(1, number_of_spots + 1):
        turtle.dot(DOT_SIZE, choice(color_tuples))
        turtle.forward(50)

        if i % 10 == 0:
            start_new_line(turtle)

    screen.exitonclick()


draw_spot_painting('spot_art.jpg', 25, 100)
