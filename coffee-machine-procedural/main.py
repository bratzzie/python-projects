from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money_inserted = 0


def print_resources():
    print(f"Water: {resources.get('water')}\n"
          f"Milk: {resources.get('milk')}\n"
          f"Coffee: {resources.get('coffee')}\n"
          f"Money: €{total_money_inserted}")


def check_resources_availability(required_resources):
    for item in required_resources:
        if resources.get(item) < required_resources.get(item):
            print(f"Sorry there is not enough {item}.")
            return False

    return True


def insert_money():
    print("Please insert coins.")
    inserted_money = 0
    inserted_money += int(input("How many 2 Euro coins?: ")) * 2
    inserted_money += int(input("How many 1 Euro coins?: ")) * 1
    inserted_money += int(input("How many 50 cents coins?: ")) * 0.50
    inserted_money += int(input("How many 20 cents coins?: ")) * 0.20
    inserted_money += int(input("How many 10 cents coins?: ")) * 0.10
    return inserted_money


def check_transaction_success(inserted_money, cost):
    if inserted_money >= cost:
        globals()["total_money_inserted"] += cost
        if inserted_money > cost:
            print(f"Here is {(round(inserted_money - cost, 2))} euros in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def deduct_resources(required_resources):
    for item in required_resources:
        resources[item] -= required_resources[item]


def process_drink(coffee_choice):
    if check_resources_availability(MENU.get(coffee_choice).get("ingredients")):
        if check_resources_availability(MENU.get(coffee_choice).get("ingredients")):
            inserted_money = insert_money()
            if check_transaction_success(inserted_money, MENU.get(coffee_choice).get("cost")):
                deduct_resources(MENU.get(coffee_choice).get("ingredients"))
                print(f"Here is your ☕ {coffee_choice.capitalize()}. Enjoy!")


def run_coffee_machine():
    print(logo)

    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "espresso" or choice == "latte" or choice == "cappuccino":
            process_drink(choice)
        elif choice == "report":
            print_resources()
        elif choice == "end":
            exit()
        else:
            print("We don't have such! Sorry.")


run_coffee_machine()
exit()
