#!/usr/bin/python3
"""
This script demonstrates the use of a simple addition function imported from another module.

The script performs the following steps:
1. Imports the `add` function from the `add_0` module.
2. Defines two variables, `a` and `b`, with values 1 and 2, respectively.
3. Uses the `add` function to calculate the sum of `a` and `b`.
4. Prints the result in the format "a + b = result".

Usage:
    Run this script directly to see the output of the addition.
    Ensure that the `add_0` module is in the same directory or in the Python path.

Example:
    $ ./your_script_name.py
    1 + 2 = 3
"""
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
