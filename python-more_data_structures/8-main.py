#!/usr/bin/python3
"""
This script demonstrates the use of the `simple_delete` and `print_sorted_dictionary` functions from the `8-simple_delete` and `6-print_sorted_dictionary` modules, respectively.

The `simple_delete` function removes a key from a dictionary if it exists. The `print_sorted_dictionary` function prints the keys and values of a dictionary in sorted order by keys.

Functions:
    simple_delete(a_dictionary, key): Removes the key from `a_dictionary` if it exists.
    print_sorted_dictionary(a_dictionary): Prints the keys and values of `a_dictionary` sorted by keys.

Example:
    The script initializes a dictionary `a_dictionary` with several key-value pairs. It then calls the `simple_delete` function to remove a specified key from the dictionary and prints the dictionary using the `print_sorted_dictionary` function.

    The script demonstrates deleting an existing key and attempting to delete a non-existent key, and prints the dictionary before and after each deletion.

Usage:
    Run the script using a Python interpreter.
"""

# Import the simple_delete and print_sorted_dictionary functions
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

# Initialize a dictionary with several key-value pairs
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }

# Remove the 'track' key from the dictionary
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")

# Attempt to remove a non-existent key 'c_is_fun' from the dictionary
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
