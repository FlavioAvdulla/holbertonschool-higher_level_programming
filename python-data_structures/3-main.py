#!/usr/bin/python3
"""
This script demonstrates importing a function from another module and using it to print a list of integers in reverse order.

The script imports the `print_reversed_list_integer` function from the module named '3-print_reversed_list_integer'.
It then creates a list of integers and uses the imported function to print each integer in the list in reverse order.

Example:
    $ ./import_and_print_reversed.py
    5
    4
    3
    2
    1
"""

print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
