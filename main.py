from art import logo

import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return int(n1 / n2)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


def calculator():
    print(logo)

    n1 = int(input("Enter the first number n1="))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        n2 = int(input("Enter the second number n2="))

        function = operations[operation_symbol]
        answer = function(n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}:, or type 'n' to start a new calculation: ") == "y":
            n1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()
