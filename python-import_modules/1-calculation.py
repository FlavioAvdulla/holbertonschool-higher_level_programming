#!/usr/bin/python3

"""
Script Documentation

Overview:
This Python script performs basic arithmetic operations (addition, subtraction, multiplication, and division) using functions imported from the `calculator_1` module. It then prints the results of these operations.

Modules Used:
- calculator_1: This module contains the arithmetic functions `add`, `sub`, `mul`, and `div`.

Variables:
- a: An integer value, set to 10.
- b: An integer value, set to 5.

Functions:
- add(a, b): Returns the sum of `a` and `b`.
- sub(a, b): Returns the difference when `b` is subtracted from `a`.
- mul(a, b): Returns the product of `a` and `b`.
- div(a, b): Returns the quotient when `a` is divided by `b`.

Logic:
1. Import the necessary functions from the `calculator_1` module.
2. Define the variables `a` and `b`.
3. Perform the arithmetic operations using the imported functions and print the results in a formatted string.
4. The `if __name__ == "__main__":` block is included to allow the script to be run as a standalone program.
"""

from calculator_1 import add, sub, mul, div

# Define the variables
a = 10
b = 5

# Perform arithmetic operations and print the results
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))

# Ensure the script can be run as a standalone program
if __name__ == "__main__":
    pass
