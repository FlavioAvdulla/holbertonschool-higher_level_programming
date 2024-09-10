#!/usr/bin/python3
"""
This script demonstrates importing a function from another module and using it to print a list of integers.

The script imports the `print_list_integer` function from the module named '0-print_list_integer'.
It then creates a list of integers and uses the imported function to print each integer in the list.

Example:
    $ ./import_and_print.py
    1
    2
    3
    4
    5
"""

print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
