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

def report(_title: str, _subtitle: str, headings, content):
    printable_report = ""
    clear_screen()
    title(_title)
    if _subtitle != "":
        subtitle(_subtitle)
    else:
        print("\n" * 1)
    column_widths = []
    heading_line = " "
    for index, heading in enumerate(headings):
        item_lengths = [len(str(item[index])) for item in content]
        item_lengths.append(len(heading))
        column_widths.append(max(item_lengths))
        heading_line += heading + " " * (column_widths[index] - len(heading) + 4)
    print(heading_line)
    printable_report += "\n" + heading_line
    print("-" * TERMINAL_WIDTH)
    printable_report += "\n" + "-" * TERMINAL_WIDTH
    for item in content:
        item_line = " "
        for index, data in enumerate(item):
            str_data = str(data)
            item_line += str_data + " " * (column_widths[index] - len(str_data) + 4)
        print(item_line)
        printable_report += "\n" + item_line
    print("\n" * (TERMINAL_HEIGHT - 10 - len(content)))
    print("=" * TERMINAL_WIDTH)
    printable_report += "\n" + "=" * TERMINAL_WIDTH
    printable_report += "\n" + "End of Report."
    return printable_report