#!/usr/bin/python3
"""
This script imports the 'pow' function from a module named '11-pow' and uses it to print the results of various power operations.

Modules:
    __import__: A built-in function used to import the '11-pow' module dynamically.

Functions:
    pow(a, b): Returns the result of a raised to the power of b. This function is imported from the '11-pow' module.

Usage:
    Run the script directly to see the output.

Example:
    $ ./script.py
    4
    9604
    1
    0.0001
    -1024
"""

# Import the 'pow' function from the '11-pow' module
pow = __import__('11-pow').pow

# Print the results of various power operations using the 'pow' function
print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
