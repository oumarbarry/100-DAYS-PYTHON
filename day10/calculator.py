from typing import Dict
from art import logo

add = lambda n1, n2: n1+n2
sub = lambda n1, n2: n1-n2
mul = lambda n1, n2: n1*n2
div = lambda n1, n2: n1/n2

operations: Dict = {'+': add, '-': sub, '*': mul, '/': div}

def calculator():
    print(logo)
    first = float(input("What's the first number ? "))

    while True:
        symbol = input("Pick an operation (+\t-\t*\t\\): ")
        second = float(input("What's the next number ? "))

        answer = operations[symbol](first, second)
        print(f"{first} {symbol} {second} = {answer}")

        keep = input(f"""Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: """)
        if keep == 'n': calculator()
        else: first = answer
        
calculator()