#!/usr/bin/python3
"""
This script prints the numbers from 0 to 99 in a comma-separated format, with each number formatted to two digits.

Modules:
    None

Functions:
    None

Variables:
    None

Usage:
    Run the script directly to see the output.

Example:
    $ ./script.py
    00, 01, 02, ..., 98, 99
"""

# Loop through numbers from 0 to 99
for n in range(100):
    # Print each number formatted to two digits, followed by a comma and space, except for the last number
    if n < 99:
        print("{:02d}, ".format(n), end='')
    else:
        print("{:02d}".format(n))
