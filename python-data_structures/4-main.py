#!/usr/bin/python3
"""
This script demonstrates importing a function from another module and using it to create a new list with an element replaced at a specific index.

The script imports the `new_in_list` function from the module named '4-new_in_list'.
It then creates a list of integers and uses the imported function to replace an element at a specified index with a new element.
Finally, it prints the new list and the original list to show the changes.

Example:
    $ ./import_and_replace_new.py
    [1, 2, 3, 9, 5]
    [1, 2, 3, 4, 5]
"""

new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
