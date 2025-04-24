from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calc(n1, n2, n3):
    if n3 == "+":
        return add(n1, n2)
    elif n3 == "-":
        return subtract(n1, n2)
    elif n3 == "*":
        return multiply(n1, n2)
    elif n3 == "/":
        return divide(n1, n2)
    else:
        print("Invalid Operation")

def calculator():
    print(logo)
    is_continue = "y"
    res = 0
    f_n = float(input("What's the first number?: "))
    while is_continue == "y":
        operator_arr = ["+", "-", "*", "/"]
        print(*operator_arr, sep="\n")
        operation = input("Pick an operation: ")
        s_n = float(input("What's the next number?: "))
        res = calc(f_n, s_n, operation)
        print(f"{f_n} {operation} {s_n} = {res}")
        is_continue = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new conversation ")
        if is_continue == "y":
            f_n = res
        else:
            calculator()
            print("\n"*20)

calculator()