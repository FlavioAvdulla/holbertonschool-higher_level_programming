#!/usr/bin/python3
"""
This script demonstrates importing a function from another module and using it to retrieve an element from a list at a specific index.

The script imports the `element_at` function from the module named '1-element_at'.
It then creates a list of integers and uses the imported function to retrieve and print the element at a specified index.

Example:
    $ ./import_and_retrieve.py
    Element at index 3 is 4
"""

element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
