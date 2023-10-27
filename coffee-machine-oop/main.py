from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def process_drink(coffee_choice):
    drink = menu.find_drink(coffee_choice)
    if drink == None:
        return

    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


def run_coffee_machine():
    while True:
        choice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if choice in menu.get_items():
            process_drink(choice)
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == "end":
            exit()
        else:
            print("We don't have such! Sorry.")


run_coffee_machine()
exit()
