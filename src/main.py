import sys
sys.path.append("modules")     # helps to import modules from main.py and tests
import modules.display as display
import modules.stock_item as stock_item


title = "Warehouse Inventory Manager"

stock = []
products = {}

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


def form(subtitle: str, form_inputs, function):
    while True:
        user_inputs = []
        for form_input_index, form_input in enumerate(form_inputs):
            exit_flag = False
            user_input = ""
            while not exit_flag:
                display.form(title, subtitle, form_inputs, form_input_index, user_inputs)
                user_input = input("Enter value: ")
                try:
                    user_input = int(user_input)
                except (ValueError):
                    pass
                else:
                    if user_input == 0:
                        exit_flag = True
                break
                
            if exit_flag:
                return
            user_inputs.append(user_input)
        display.form(title, subtitle, form_inputs, len(form_inputs), user_inputs)
        user_input = input("Press enter to confirm or '0' to cancel: ")
        try:
            user_input = int(user_input)
            if user_input == 0:
                return
        except (ValueError):
            pass
        
        display.form(title, subtitle, form_inputs, len(form_inputs), user_inputs)
        try:
            function(*user_inputs)
        except (ValueError):
            input("Values entered are not compatible, please try again:")
            continue
        else:
            input("Successful!")
            break


def add_product(number: int, name: str):
    if not isinstance(number, int) or not isinstance(name, str):
        raise ValueError()
    products[number] = name
    report()

"""
All of the menu options for the app, along with functions to call when options
are selected, and arguments. menu function is called recursively so menus at 
greater depth are described first.
"""
add_product_inputs = ["Product Number",
                      "Product Name"]

product_options = ["View Products",
                   "Add Product",
                   "Edit Product",
                   "Remove Product"]
product_option_functions = [[report, []],
                            [form, [product_options[1], add_product_inputs, add_product]],
                            [form, [product_options[2], add_product_inputs, print]],
                            [form, [product_options[3], add_product_inputs, print]]]

stock_options = ["View Stock",
                 "Add Stock",
                 "Move Stock",
                 "Remove Stock"]
stock_option_functions = [[report, []],
                          [form, [stock_options[1], print]],
                          [form, [stock_options[2], print]],
                          [form, [stock_options[3], print]]]

options = ["Products",
           "Stock"]
option_functions = [[menu, [options[0], product_options, product_option_functions]],
                    [menu, [options[1], stock_options, stock_option_functions]]]


# Main block here
if __name__ == '__main__':
    menu("Main Menu", options, option_functions)
    display.clear_screen()
