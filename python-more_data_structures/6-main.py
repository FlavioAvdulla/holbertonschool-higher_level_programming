#!/usr/bin/python3
"""
This script demonstrates the use of the `print_sorted_dictionary` function from the `6-print_sorted_dictionary` module.

The `print_sorted_dictionary` function takes a dictionary and prints its keys and values in sorted order by keys.

Functions:
    print_sorted_dictionary(a_dictionary): Prints the keys and values of `a_dictionary` sorted by keys.

Example:
    The script initializes a dictionary `a_dictionary` with several key-value pairs. It then calls the `print_sorted_dictionary` function to print the dictionary's keys and values in sorted order.

Usage:
    Run the script using a Python interpreter.
"""

# Import the print_sorted_dictionary function from the 6-print_sorted_dictionary module
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

# Initialize a dictionary with several key-value pairs
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }

# Print the dictionary's keys and values in sorted order
print_sorted_dictionary(a_dictionary)
