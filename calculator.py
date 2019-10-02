"""A prefix-notation calculator."""

from arithmetic import *

def greet_player():
    """greets player"""
    print("Hi Player! Welcome to the calculator.")

def turn_str_into_int(l):
    """takes list and turns string numbers into integers"""
    operator_list = ["+", "-", "*", "/", "**", "squares", "cubes", "pows", "%"]
    
    new_list = []
    for item in l:
        if item in operator_list:
            new_list.append(item)

        if item.isdigit():
            new_list.append(int(item))
        else:
            new_list.append(item) 
    return new_list

def play_calculator(a):
    """calls calculation functions based on user input"""
    
    a = turn_str_into_int(a.split(" "))

    if a[0] == "+":
        print(add(a[1], a[2]))
    elif a[0] == "-":
        print(subtract(a[1], a[2]))
    elif a[0] == "*":
        print(multiply(a[1], a[2]))
    elif a[0] == "/":
        print(divide(a[1], a[2]))
    elif a[0] == "**" and a[2] == 2 or a[0] == "squares":
        print(square(a[1]))
    elif a[0] == "**" and a[2] == 3 or a[0] == "cubes":
        print(cube(a[1]))
    elif a[0] == "**" and not a[2] == 2 and not a[2] == 3 or a[0] == "pows":
        print(power(a[1], a[2]))
    elif a[0] == "%":
        print(mod(a[1], a[2]))
    else:
        print("Sorry cannot compute! Try again.")

def continue_game(b_input):
    """takes user input to return true or false for continuing game"""
    if b_input.upper() == "NO":
        print("Goodbye!")
        return False
    else:
        return True

def calculate():
    """main calculator function"""
    greet_player()

    while True:
       
        play_calculator(a = input("What is your calculation? Please enter the operator first, followed by the numbers. Leave spaces between your entries. > "))
        repeat_calc = continue_game(b_input = input("Would you like to play again?"))
        if repeat_calc == False:
            break

calculate()