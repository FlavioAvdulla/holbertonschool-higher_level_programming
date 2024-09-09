#!/usr/bin/python3
"""
This script prints all unique combinations of two digits in ascending order, formatted as two-digit numbers, separated by commas and spaces.

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
    01, 02, 03, ..., 89, 90
"""

# Loop through the first digit from 0 to 9
for i in range(10):
    # Loop through the second digit from i+1 to 9
    for j in range(i + 1, 10):
        # Print each combination formatted as two-digit numbers
        if i < 8 or j < 9:
            print("{:02d}, ".format(i * 10 + j), end='')
        else:
            print("{:02d}".format(i * 10 + j))
