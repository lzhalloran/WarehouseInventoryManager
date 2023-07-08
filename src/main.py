import os
import sys
sys.path.append("modules")
terminal_width = 80
terminal_height = 24
title = "Warehouse Inventory Manager"


os.system('cls||clear')
print("-" * terminal_width)
print(" " * int((terminal_width/2 - len(title)/2)) + title)
print("-" * terminal_width)
print("\n" * (terminal_height - 6))
print("_" * terminal_width)
input()
os.system('cls||clear')