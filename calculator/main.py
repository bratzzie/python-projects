from art import logo


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    run = True

    num1 = float(input("Enter the first number: "))

    for operator in operations:
        print(operator)

    while run:
        chosen_operator = input(
            "Choose an operator from the operators above: ")
        num2 = float(input("Enter the next number: "))
        answer = operations[chosen_operator](num1, num2)
        print(f"{num1} {chosen_operator} {num2} = {answer}")

        if input(
                f"Do you want to continue calculating with {answer}? Or type 'n' to start new calculation (y/n): "
        ) == "y":
            num1 = answer
        else:
            run = False
            calculator()


calculator()
exit()
