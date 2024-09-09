#!/usr/bin/python3
"""
This script demonstrates the use of basic arithmetic functions imported from another module.

The script performs the following steps:
1. Imports the `add`, `sub`, `mul`, and `div` functions from the `calculator_1` module.
2. Defines two variables, `a` and `b`, with values 10 and 5, respectively.
3. Uses the imported functions to perform addition, subtraction, multiplication, and division on `a` and `b`.
4. Prints the results in the format "a operator b = result".

Usage:
    Run this script directly to see the output of the arithmetic operations.
    Ensure that the `calculator_1` module is in the same directory or in the Python path.

Example:
    $ ./your_script_name.py
    10 + 5 = 15
    10 - 5 = 5
    10 * 5 = 50
    10 / 5 = 2.0
"""
from calculator_1 import add, sub, mul, div

a = 10
b = 5

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))

if __name__ == "__main__":
    pass
