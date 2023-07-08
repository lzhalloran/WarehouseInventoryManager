import os
import sys
sys.path.append("modules")

TERMINAL_WIDTH = 80
TERMINAL_HEIGHT = 24
title = "Warehouse Inventory Manager"

def clear_screen():
    os.system('cls||clear')

def display_title():
    print("=" * TERMINAL_WIDTH)
    print(" " * int((TERMINAL_WIDTH/2 - len(title)/2)) + title)
    print("=" * TERMINAL_WIDTH)

def display_subtitle(subtitle : str):
    print(" " * int((TERMINAL_WIDTH/2 - len(subtitle)/2)) + subtitle)
    print("-" * TERMINAL_WIDTH)

def display_option(number: int, text: str):
    print(" " * int((TERMINAL_WIDTH/2 - 12)) + "[" + str(number) + "] - " + text + "\n")


def display_main_menu():
    clear_screen()
    display_title()
    print("\n" * 4)
    display_option(1, "Products")
    display_option(2, "Stock")
    display_option(0, "Exit")
    print("\n" * (TERMINAL_HEIGHT - 17))
    print("=" * TERMINAL_WIDTH)

def display_stock_menu():
    clear_screen()
    display_title()
    display_subtitle("Stock")
    print("\n" * 2)
    display_option(1, "View Stock")
    display_option(2, "Add Stock")
    display_option(3, "Remove Stock")
    display_option(0, "Exit")
    print("\n" * (TERMINAL_HEIGHT - 19))
    print("=" * TERMINAL_WIDTH)

def display_product_menu():
    clear_screen()
    display_title()
    display_subtitle("Product")
    print("\n" * 2)
    display_option(1, "View Products")
    display_option(2, "Add Product")
    display_option(3, "Edit Product")
    display_option(4, "Remove Product")
    display_option(0, "Exit")
    print("\n" * (TERMINAL_HEIGHT - 21))
    print("=" * TERMINAL_WIDTH)

def stock_menu():
    user_input = ""
    while True:
        display_stock_menu()
        try:
            user_input = int(input("Choose option: "))
        except(ValueError):
            continue

        match user_input:
            case 0:
                break

def product_menu():
    user_input = ""
    while True:
        display_product_menu()
        try:
            user_input = int(input("Choose option: "))
        except(ValueError):
            continue

        match user_input:
            case 0:
                break

user_input = ""
while True:
    display_main_menu()
    try:
        user_input = int(input("Choose option: "))
    except(ValueError):
        continue

    match user_input:
        case 1:
            product_menu()
        case 2:
            display_stock_menu()
            stock_menu()
        case 0:
            break


clear_screen()
