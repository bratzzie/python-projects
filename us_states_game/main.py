import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

writing_t = turtle.Turtle()
writing_t.hideturtle()
writing_t.penup()

states_df = pd.read_csv("50_states.csv")
states_list = states_df.state.to_list()

users_state = screen.textinput(title="Guess The State", prompt="What state's name do you know?").title()
guessed_states = []

while len(guessed_states) < 50:
    if users_state == "Exit":
        not_guessed_states = [state for state in states_list if state not in guessed_states]
        not_guessed_states_df = pd.DataFrame(not_guessed_states)
        not_guessed_states_df.to_csv("not_guessed_states.csv")
        break
    if users_state in states_list:
        guessed_states.append(users_state)
        state_df = states_df[states_df.state == users_state]
        writing_t.goto(int(state_df.x), int(state_df.y))
        writing_t.write(users_state)
    users_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="What's another state's name?").capitalize()
