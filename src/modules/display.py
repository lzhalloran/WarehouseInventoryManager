import os

TERMINAL_WIDTH = 80
TERMINAL_HEIGHT = 24


def clear_screen():
    os.system('cls||clear')


def title(title: str):
    print("=" * TERMINAL_WIDTH)
    print(" " * int((TERMINAL_WIDTH/2 - len(title)/2)) + title)
    print("=" * TERMINAL_WIDTH)


def subtitle(subtitle: str):
    print(" " * int((TERMINAL_WIDTH/2 - len(subtitle)/2)) + subtitle)
    print("-" * TERMINAL_WIDTH)


def option(number: int, text: str):
    print(" " * int((TERMINAL_WIDTH/2 - 12)) + "[" + str(number) + "] - " + text + "\n")

def menu(_title: str, _subtitle: str, options):
    clear_screen()
    title(_title)
    if _subtitle != "":
        subtitle(_subtitle)
        print("\n" * 2)
    else:
        print("\n" * 4)
    for option_index, option_value in enumerate(options):
        option(option_index + 1, option_value)
    option(0, "Exit")
    print("\n" * (TERMINAL_HEIGHT - 13 - (2 * len(options))))
    print("=" * TERMINAL_WIDTH)

def form(_title: str, _subtitle: str, inputs, input_index: int, user_inputs):
    clear_screen()
    title(_title)
    line_counter = 0
    if _subtitle != "":
        subtitle(_subtitle)
        print("\n" * 2)
    else:
        print("\n" * 4)
    for i in range(input_index):
        print(" " * int((TERMINAL_WIDTH/2 - 12)) + f"{inputs[i]}: {user_inputs[i]}\n")
        line_counter += 2
    if input_index != len(inputs):
        print(" " * int((TERMINAL_WIDTH/2 - 12)) + f"{inputs[input_index]}: _________\n")
        line_counter += 2
    
    print("\n")
    line_counter += 2
    option(0, "Exit")
    print("\n" * (TERMINAL_HEIGHT - 13 - line_counter))
    print("=" * TERMINAL_WIDTH)