#!/usr/bin/python3
"""
This script demonstrates the use of the `search_replace` function from the `1-search_replace` module.

The `search_replace` function takes a list and replaces all occurrences of a specified element with a new element.

Functions:
    search_replace(my_list, search, replace): Replaces all occurrences of `search` in `my_list` with `replace`.

Example:
    The script initializes a list `my_list` with several integers. It then calls the `search_replace` function to replace all occurrences of the integer `2` with `89`. The modified list is stored in `new_list`.

    Finally, the script prints both the modified list (`new_list`) and the original list (`my_list`).

Usage:
    Run the script using a Python interpreter.
"""

# Import the search_replace function from the 1-search_replace module
search_replace = __import__('1-search_replace').search_replace

# Initialize a list with several integers
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]

# Replace all occurrences of 2 with 89 in the list
new_list = search_replace(my_list, 2, 89)

# Print the modified list
print(new_list)

# Print the original list
print(my_list)
