#!/usr/bin/python3
"""
This script prints the numbers from 0 to 98 along with their hexadecimal representation.

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
    0 = 0x0
    1 = 0x1
    2 = 0x2
    ...
    98 = 0x62
"""

# Loop through numbers from 0 to 98
for n in range(99):
    # Print each number and its hexadecimal representation
    print("{} = 0x{:x}".format(n, n))
