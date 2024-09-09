#!/usr/bin/python3
"""
This script imports the 'add' function from a module named '10-add' and uses it to print the sum of several pairs of numbers.

Modules:
    __import__: A built-in function used to import the '10-add' module dynamically.

Functions:
    add(a, b): Returns the sum of a and b. This function is imported from the '10-add' module.

Usage:
    Run the script directly to see the output.

Example:
    $ ./script.py
    3
    98
    98
"""

# Import the 'add' function from the '10-add' module
add = __import__('10-add').add

# Print the sum of various pairs of numbers using the 'add' function
print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
