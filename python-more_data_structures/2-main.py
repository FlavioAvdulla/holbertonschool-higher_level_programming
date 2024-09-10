#!/usr/bin/python3
"""
This script demonstrates the use of the `uniq_add` function from the `2-uniq_add` module.

The `uniq_add` function takes a list of integers and returns the sum of all unique integers in the list.

Functions:
    uniq_add(my_list): Returns the sum of unique integers in `my_list`.

Example:
    The script initializes a list `my_list` with several integers, including duplicates. It then calls the `uniq_add` function to calculate the sum of all unique integers in the list. The result is stored in `result`.

    Finally, the script prints the result.

Usage:
    Run the script using a Python interpreter.
"""

# Import the uniq_add function from the 2-uniq_add module
uniq_add = __import__('2-uniq_add').uniq_add

# Initialize a list with several integers, including duplicates
my_list = [1, 2, 3, 1, 4, 2, 5]

# Calculate the sum of unique integers in the list
result = uniq_add(my_list)

# Print the result
print("Result: {:d}".format(result))
