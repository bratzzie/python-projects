from random import choice
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return choice(cards)


def add_two_random_cards(cards):
    for _ in range(2):
        cards.append(deal_card())
    return cards


def compare(user_score, computer_score):
    if computer_score == 0:
        return ("You lose, opponent has a Blackjack!")

    if user_score == 0:
        return ("You won with a Blackjack!")

    if user_score == computer_score:
        return ("It's a draw.")

    if user_score > 21:
        return ("You lost, by going over.")

    if computer_score > 21:
        return ("You won, opponent went over.")

    if user_score > computer_score:
        return ("You won.")
    else:
        return ("You lost.")


def calculate_score(cards):
    score = sum(cards)

    if len(cards) == 2 and score == 21:
        return 0
    elif score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return calculate_score(cards)

    return score


def play():
    user_cards = []
    computer_cards = []
    is_game_over = False

    user_cards = add_two_random_cards(user_cards)
    computer_cards = add_two_random_cards(computer_cards)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input(
                    "Type 'y' to get another card, type 'n' to pass: ") == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}"
    )
    print(compare(user_score, computer_score))


def run():
    while input("Do you want to play a game of Blackjack? Type (y/n)") == "y":
        clear()
        print(logo)
        play()
    else:
        exit()


run()
