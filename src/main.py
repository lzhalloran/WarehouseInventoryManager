import os
import sys
sys.path.append("modules")

TERMINAL_WIDTH = 80
TERMINAL_HEIGHT = 24
title = "Warehouse Inventory Manager"

def clear_screen():
    os.system('cls||clear')

def display_title():
    print("-" * TERMINAL_WIDTH)
    print(" " * int((TERMINAL_WIDTH/2 - len(title)/2)) + title)
    print("-" * TERMINAL_WIDTH)

def display_option(number: int, text: str):
    print(" " * int((TERMINAL_WIDTH/2 - 10)) + "[" + str(number) + "] - " + text + "\n")


def display_main_menu():
    display_title()
    print("\n" * 6)
    display_option(1, "Products")
    display_option(2, "Stock")
    display_option(3, "Exit")
    print("\n" * (TERMINAL_HEIGHT - 19))
    print("_" * TERMINAL_WIDTH)

user_input = ""
while(user_input != "3"):
    clear_screen()
    display_main_menu()
    user_input = input("Choose option: ")

clear_screen()
