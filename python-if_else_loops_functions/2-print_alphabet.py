#!/usr/bin/python3
"""
This script prints the lowercase English alphabet from 'a' to 'z' without spaces or newlines.

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
    abcdefghijklmnopqrstuvwxyz
"""

# Loop through the ASCII values for lowercase letters 'a' to 'z'
for alphabet in range(97, 123):
    # Print each character without a newline
    print("{}".format(chr(alphabet)), end="")
