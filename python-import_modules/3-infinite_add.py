#!/usr/bin/python3
"""
This script imports a variable from another module and prints its value.

Modules:
    variable_load_5: A module that contains the variable `a`.

Usage:
    Run this script from the command line.
    Example:
        $ ./script_name.py

    Output:
        - Prints the value of the variable `a` imported from the module `variable_load_5`.
"""

if __name__ == "__main__":
    from variable_load_5 import a
    print(a)
