from turtle import Turtle, Screen
import random
from tkinter import Tk, Button, Label

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_positions = [-70.0, -40.0, -10.0, 20.0, 50.0, 80.0]
START_INDEX = -230.0
FINISH_INDEX = 230.0
MAX_STEP_DISTANCE = 10
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400


def create_turtles(turtles_list):
    for t in range(0, 6):
        new_turtle = Turtle("turtle")
        new_turtle.penup()
        new_turtle.color(colors[t])
        new_turtle.goto(START_INDEX, y_positions[t])
        turtles_list.append(new_turtle)


def display_pop_up(msg):
    popup = Tk()
    popup.wm_title("Race is ended...")
    popup.wm_minsize(250, 50)
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    button = Button(popup, text="Okay!", command=popup.destroy)
    button.pack()
    popup.mainloop()


def run():
    is_race = False
    screen = Screen()
    screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

    all_turtles = []
    create_turtles(all_turtles)

    if user_bet and user_bet in colors:
        is_race = True
    else:
        display_pop_up("Such turtle doesnt participate in the race. Sorry!")

    while is_race:
        for turtle in all_turtles:
            if turtle.xcor() > FINISH_INDEX:
                is_race = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    display_pop_up(f"You have won! The {winner} is the winner!")
                else:
                    display_pop_up(f"You have lost! The {winner} is the winner!")
            else:
                random_distance = random.randint(0, MAX_STEP_DISTANCE)
                turtle.forward(random_distance)

    screen.exitonclick()


run()
