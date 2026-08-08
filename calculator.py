def add(n1, n2):
    return n1 + n2

def subtres(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    '+': add,
    '-': subtres,
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
        num2 = float(input("Enter second number: "))
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