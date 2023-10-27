from art import logo, vs
from game_data import data
from random import choice
from replit import clear

COMPARE_A = "Compare A: "
COMPARE_B = "Against B: "

WRONG_STR = "Sorry, that's wrong. Final score: "
CORRECT_STR = "You're right! Current score: "


def get_random_account():
    return choice(data)


def account_to_string(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}."


def check_guess(guess, account_a, account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    is_lost = False
    user_guessed = ""

    while not is_lost:
        random_a = get_random_account()
        random_b = get_random_account()
        if random_a == random_b:
            random_b = data[data.index(random_b) + 1]

        clear()
        print(logo)
        print(user_guessed)
        print(f"{COMPARE_A} {account_to_string(random_a)}")
        print(vs)
        print(f"{COMPARE_B} {account_to_string(random_b)}")

        user_choice = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
        if check_guess(user_choice, random_a, random_b):
            score += 1
            user_guessed = f"{CORRECT_STR}{score}."
        else:
            is_lost = True
            user_guessed = f"{WRONG_STR}{score}."

        clear()
        print(logo)
        print(user_guessed)
  
game()
exit()
