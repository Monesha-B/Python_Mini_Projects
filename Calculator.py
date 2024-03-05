from ASCII_ART_Calculator import logo
from replit import clear

# add
def add(a, b):
    return a+b

# subtract
def subtract(a, b):
    return a-b

# multiply
def multiply(a, b):
    return a*b

# divide
def divide(a, b):
    return a/b    


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

# function = operations["*"]
# print(function(2, 2))
def recursive_calculation():
    print(logo)
    number1 = float(input("Enter the number: ")) # first number
    for to_print_each_operator in operations:
        print(to_print_each_operator)

    continue_calculating = False

    while not continue_calculating:    
        operation_symbol = input("Pick an operation from the line above: ")  
        number2 = float(input("Enter the next number: ")) # second number

        oper = operations[operation_symbol]
        answer = oper(number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")
        user_input = input(f"Do you want to continue with {answer}, Type 'y' to continue, 'n' to start a new calculation or 'c' to exit:")
        if user_input == "y":
            number1 = answer
        elif user_input == 'n':
            clear()
            recursive_calculation()        
        elif user_input == 'c':
            continue_calculating = True

recursive_calculation()       
    # operation_symbol = input("Pick an operation from the line above: ")  
    # number3 = int(input("Enter the third number: "))

    # oper = operations[operation_symbol]
    # answer1 = oper(answer, number3)
    # print(f"{answer} {operation_symbol} {number3} = {answer1}")