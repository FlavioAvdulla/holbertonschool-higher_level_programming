#!/usr/bin/python3
"""
This script demonstrates the use of the `multiply_by_2` and `print_sorted_dictionary` functions from the `9-multiply_by_2` and `6-print_sorted_dictionary` modules, respectively.

The `multiply_by_2` function takes a dictionary and returns a new dictionary with all values multiplied by 2. The `print_sorted_dictionary` function prints the keys and values of a dictionary in sorted order by keys.

Functions:
    multiply_by_2(a_dictionary): Returns a new dictionary with all values multiplied by 2.
    print_sorted_dictionary(a_dictionary): Prints the keys and values of `a_dictionary` sorted by keys.

Example:
    The script initializes a dictionary `a_dictionary` with several key-value pairs. It then calls the `multiply_by_2` function to create a new dictionary with all values multiplied by 2 and prints both the original and the new dictionary using the `print_sorted_dictionary` function.

Usage:
    Run the script using a Python interpreter.
"""

# Import the multiply_by_2 and print_sorted_dictionary functions
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

# Initialize a dictionary with several key-value pairs
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}

# Create a new dictionary with all values multiplied by 2
new_dict = multiply_by_2(a_dictionary)

# Print the original dictionary's keys and values in sorted order
print_sorted_dictionary(a_dictionary)
print("--")
# Print the new dictionary's keys and values in sorted order
print_sorted_dictionary(new_dict)
