#!/usr/bin/python3
"""
This script demonstrates the use of the `update_dictionary` and `print_sorted_dictionary` functions from the `7-update_dictionary` and `6-print_sorted_dictionary` modules, respectively.

The `update_dictionary` function updates a dictionary with a new key-value pair or modifies an existing key with a new value. The `print_sorted_dictionary` function prints the keys and values of a dictionary in sorted order by keys.

Functions:
    update_dictionary(a_dictionary, key, value): Updates `a_dictionary` with the key-value pair (`key`, `value`).
    print_sorted_dictionary(a_dictionary): Prints the keys and values of `a_dictionary` sorted by keys.

Example:
    The script initializes a dictionary `a_dictionary` with several key-value pairs. It then calls the `update_dictionary` function to update the dictionary with new key-value pairs and prints the updated dictionary using the `print_sorted_dictionary` function.

    The script demonstrates updating an existing key and adding a new key to the dictionary, and prints the dictionary before and after each update.

Usage:
    Run the script using a Python interpreter.
"""

# Import the update_dictionary and print_sorted_dictionary functions
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

# Initialize a dictionary with several key-value pairs
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }

# Update the dictionary with a new value for an existing key
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

# Update the dictionary with a new key-value pair
new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
