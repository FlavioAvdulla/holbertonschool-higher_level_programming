#!/usr/bin/python3
"""
This script demonstrates importing a function from another module and using it to find the maximum integer in a list.

The script imports the `max_integer` function from the module named '9-max_integer'.
It then creates a list of integers and uses the imported function to find the maximum value in the list.
Finally, it prints the maximum value.

Example:
    $ ./import_and_find_max.py
    Max: 90
"""

max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
