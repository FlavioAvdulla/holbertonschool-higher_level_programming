#!/usr/bin/python3
"""
This script demonstrates swapping the values of two variables and printing the result.

The script initializes two variables, `a` and `b`, with the values 89 and 10, respectively.
It then swaps their values and prints the result in the format "a=<value> - b=<value>".

Example:
    $ ./swap_variables.py
    a=10 - b=89
"""

a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
