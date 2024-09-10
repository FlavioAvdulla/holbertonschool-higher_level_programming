#!/usr/bin/python3
"""
This script demonstrates the use of the `number_keys` function from the `5-number_keys` module.

The `number_keys` function takes a dictionary and returns the number of keys in the dictionary.

Functions:
    number_keys(a_dictionary): Returns the number of keys in `a_dictionary`.

Example:
    The script initializes a dictionary `a_dictionary` with several key-value pairs. It then calls the `number_keys` function to count the number of keys in the dictionary. The result is stored in `nb_keys`.

    Finally, the script prints the number of keys.

Usage:
    Run the script using a Python interpreter.
"""

# Import the number_keys function from the 5-number_keys module
number_keys = __import__('5-number_keys').number_keys

# Initialize a dictionary with several key-value pairs
a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }

# Count the number of keys in the dictionary
nb_keys = number_keys(a_dictionary)

# Print the number of keys
print("Number of keys: {:d}".format(nb_keys))
