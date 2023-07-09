import sys
sys.path.append("modules")
import modules.display as display

title = "Warehouse Inventory Manager"

def stock_menu():
    user_input = ""
    options = ["View Stock", "Add Stock", "Remove Stock"]
    while True:
        display.menu(title, "Stock", options)
        try:
            user_input = int(input("Choose option: "))
        except(ValueError):
            continue

        match user_input:
            case 0:
                break

def product_menu():
    user_input = ""
    options = ["View Products", "Add Products", "Edit Product", "Remove Product"]
    while True:
        display.menu(title, "Products", options)
        try:
            user_input = int(input("Choose option: "))
        except(ValueError):
            continue

        match user_input:
            case 0:
                break

user_input = ""
options = ["Products", "Stock"]
while True:
    display.menu(title, "Main Menu", options)
    try:
        user_input = int(input("Choose option: "))
    except(ValueError):
        continue

    match user_input:
        case 1:
            product_menu()
        case 2:
            stock_menu()
        case 0:
            break


display.clear_screen()
