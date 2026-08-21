def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def calculator():
    should_continue = True
    num1 = float(input("Enter first number: "))

    while should_continue:
        for symbol in operation:
            print(symbol)
        operator = input("Pick one of the following options: ")
        if operator not in operation:
            print("Invalid operation. Please pick from the list.")
            continue
        num2 = float(input("Enter second number: "))
        if operator == '/' and num2 == 0:
            print("Error! Division by zero is not allowed.")
            continue
        answer = operation[operator](num1, num2)
        print(f"{num1} {operator} {num2} ={answer}")

        choice = input(f"Type 'y' to continue with {answer} or 'n' to exit: ")
        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()