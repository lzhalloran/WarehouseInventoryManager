import sys
sys.path.append("modules")     # helps to import modules from main.py and tests
import csv
import modules.display as display
import modules.stock_item as stock_item


title = "Warehouse Inventory Manager"
stock_file_path = "data/stock.csv"
products_file_path = "data/products.csv"

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


def report(subtitle: str, headings, content_function):
    display.report(title, subtitle, headings, content_function())
    input("Enter to continue: ")


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
            input("Values entered are invalid, please try again: ")
            continue
        except (TypeError):
            input("One or more values are of wrong type, please try again: ")
        else:
            input("Successful!")
            break


def add_product(number: int, name: str):
    if not isinstance(number, int) or not isinstance(name, str):
        raise TypeError()
    elif products.get(number) is not None:
        raise ValueError()
    products[number] = name

def edit_product(number: int, name: str):
    if not isinstance(number, int) or not isinstance(name, str):
        raise TypeError()
    elif products.get(number) is None:
        raise ValueError()
    products[number] = name

def remove_product(number: int):
    if not isinstance(number, int):
        raise TypeError()
    elif products.get(number) is None:
        raise ValueError()
    elif any(item.product == number for item in stock):
        raise ValueError()
    del products[number]

def get_products_2D_array():
    return [[key, value] for key, value in products.items()]

def add_stock(number: int, product: int, room: str, row: int, height: int):
    if any(item.identifier == number for item in stock):
        raise ValueError()
    if products.get(product) is None:
        raise ValueError()
    stock.append(stock_item.StockItem(number, product, [room, row, height]))

def move_stock(number: int, room: str, row: int, height: int):
    if not any(item.identifier == number for item in stock):
        raise ValueError()
    item_to_move = next(item for item in stock if item.identifier == number)
    item_to_move.location = [room, row, height]

def remove_stock(number: int):
    if not any(item.identifier == number for item in stock):
        raise ValueError()
    item_to_remove = next(item for item in stock if item.identifier == number)
    stock.remove(item_to_remove)

def get_stock_2D_array():
    return [[item.identifier, 
             item.product,
             products[item.product],
             item.location[0], 
             item.location[1], 
             item.location[2]] for item in stock]

def save_stock():
    try:
        with open(stock_file_path, 'w') as stock_file:
            writer = csv.writer(stock_file)
            for item in stock:
                writer.writerow([item.identifier, 
                                 item.product, 
                                 item.location[0], 
                                 item.location[1], 
                                 item.location[2]])
    except (FileNotFoundError):
        return

def load_stock():
    try:
        with open(stock_file_path) as stock_file:
            reader = csv.reader(stock_file)
            for row in reader:
                stock.append(stock_item.StockItem(int(row[0]), 
                                                  int(row[1]), 
                                                  [row[2], int(row[3]), int(row[4])]))
    except (FileNotFoundError):
        return

def save_products():
    try:
        with open(products_file_path, 'w') as products_file:
            writer = csv.writer(products_file)
            for key, value in products.items():
                writer.writerow([key, value])
    except (FileNotFoundError):
        return

def load_products():
    try:
        with open(products_file_path) as products_file:
            reader = csv.reader(products_file)
            for row in reader:
                products[int(row[0])] = row[1]
    except (FileNotFoundError):
        return

"""
All of the menu options for the app, along with functions to call when options
are selected, and arguments. menu function is called recursively so menus at 
greater depth are described first.
"""
product_inputs = ["Product Number",
                      "Product Name"]

product_options = ["View Products",
                   "Add Product",
                   "Edit Product",
                   "Remove Product"]
product_option_functions = [[report, [product_options[0], product_inputs, get_products_2D_array]],
                            [form, [product_options[1], product_inputs, add_product]],
                            [form, [product_options[2], product_inputs, edit_product]],
                            [form, [product_options[3], [product_inputs[0]], remove_product]]]

stock_inputs = ["Item Number",
                "Product",
                "Room",
                "Row",
                "Height"]

stock_inputs_with_product_name = stock_inputs.copy()
stock_inputs_with_product_name[1] = "Product Number"
stock_inputs_with_product_name.insert(2, "Product Name")

stock_options = ["View Stock",
                 "Add Stock",
                 "Move Stock",
                 "Remove Stock"]
stock_option_functions = [[report, [stock_options[0], stock_inputs_with_product_name, get_stock_2D_array]],
                          [form, [stock_options[1], stock_inputs, add_stock]],
                          [form, [stock_options[2], [stock_inputs[0], stock_inputs[2], stock_inputs[3], stock_inputs[4]], move_stock]],
                          [form, [stock_options[3], [stock_inputs[0]], remove_stock]]]

options = ["Products",
           "Stock"]
option_functions = [[menu, [options[0], product_options, product_option_functions]],
                    [menu, [options[1], stock_options, stock_option_functions]]]


# Main block here
if __name__ == '__main__':
    load_products()
    load_stock()
    menu("Main Menu", options, option_functions)
    save_products()
    save_stock()
    display.clear_screen()
