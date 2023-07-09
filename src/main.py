import modules.display as display
import sys
sys.path.append("modules")

title = "Warehouse Inventory Manager"


def menu(subtitle: str, options, option_functions):
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


if __name__ == '__main__':
    user_input = ""

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

    menu("Main Menu", options, option_functions)

    display.clear_screen()
