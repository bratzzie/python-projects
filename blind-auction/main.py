from replit import clear
from art import logo


def make_bids():
    print(logo)

    bids = {}
    run = "yes"
    while run == "yes":
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        bids[name] = bid
        run = input("Are there any other bidders? Type 'yes' or 'no': ")
        if run != "yes" and run != "no":
            run = "no"
        clear()
    return bids


def find_biggest_bidder(bids):
    biggest_bid_name = ""
    biggest_bid = -1

    for key in bids:
        if bids[key] > biggest_bid:
            biggest_bid_name = key
            biggest_bid = bids[key]

    print(f"The winner is {biggest_bid_name} with a bid of ${biggest_bid}.")


bids = make_bids()
find_biggest_bidder(bids)
exit()
