import modules.display as display
import sys
sys.path.append("modules")     # helps to import modules from main.py and tests

title = "Warehouse Inventory Manager"


# Functions to handle interfacing with application

def menu(subtitle: str, options, option_functions):
    """
    Handles interface and display of menu screens, using options and their
    functions and arguments to call.
    options - list of option names to display
    option_functions - list of functions and arguments: 
    [[function1, [arg1, arg2]], 
    [function2, [arg1]]] etc.
    """
    user_input = ""
    while True:
        display.menu(title, subtitle, options)
        try:
            user_input = int(input("Choose option: "))
        except (ValueError):
            continue

        if user_input in range(1, len(options) + 1):
            option_functions[user_input -
                             1][0](*option_functions[user_input - 1][1])
        elif user_input == 0:
            break


def report():
    pass


def form():
    pass


"""
All of the menu options for the app, along with functions to call when options
are selected, and arguments. menu function is called recursively so menus at 
greater depth are described first.
"""
product_options = ["View Products",
                   "Add Products",
                   "Edit Product",
                   "Remove Product"]
product_option_functions = [[report, []],
                            [form, []],
                            [form, []],
                            [form, []]]

stock_options = ["View Stock",
                 "Add Stock",
                 "Remove Stock"]
stock_option_functions = [[report, []],
                          [form, []],
                          [form, []]]

options = ["Products",
           "Stock"]
option_functions = [[menu, [options[0], product_options, product_option_functions]],
                    [menu, [options[1], stock_options, stock_option_functions]]]


# Main block here
if __name__ == '__main__':
    menu("Main Menu", options, option_functions)
    display.clear_screen()
