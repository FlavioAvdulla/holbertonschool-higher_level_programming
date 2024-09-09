#!/usr/bin/python3
"""
This script calculates and prints the sum of command-line arguments passed to it.

Modules:
    sys: Provides access to command-line arguments.

Functions:
    main(): The main function that processes and sums the command-line arguments.

Usage:
    Run this script from the command line with any number of integer arguments.
    Example:
        $ ./script_name.py 1 2 3

    Output:
        - Prints the sum of the provided integer arguments.
"""

import sys

def main():
    """
    Processes command-line arguments, calculates their sum, and prints the result.
    """
    argv = sys.argv[1:]
    total = sum(int(arg) for arg in argv)
    print(total)

if __name__ == "__main__":
    main()
