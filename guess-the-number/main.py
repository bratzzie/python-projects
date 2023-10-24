from art import logo
from random import randint


def run():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    level = input("Choose a difficulty level. Type 'easy'/'hard': ")
    if level == "easy":
        lives = 10
    elif level == "hard":
        lives = 5

    random_number = randint(1, 100)
    guessed = False
    while lives > 0 and not guessed:
        print(f"You have {lives} attempts to guess the number.")

        guess = int(input("Make a guess: "))
        if guess > random_number:
            print("Too high.")
            lives -= 1
        elif guess < random_number:
            print("Too low.")
            lives -= 1
        else:
            guessed = True
            print(f"You got it! The hidden number is {random_number}.")

    print(f"Sorry, you lost! The hidden number is {random_number}")


run()
exit()
