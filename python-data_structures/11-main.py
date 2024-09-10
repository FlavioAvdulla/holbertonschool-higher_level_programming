#!/usr/bin/python3
"""
This script demonstrates importing a function from another module and using it to delete an element from a list at a specific index.

The script imports the `delete_at` function from the module named '11-delete_at'.
It then creates a list of integers and uses the imported function to delete an element at a specified index.
Finally, it prints the modified list and the original list to show the changes.

Example:
    $ ./import_and_delete.py
    [1, 2, 3, 5]
    [1, 2, 3, 5]
"""

delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
