#!/usr/bin/python3
"""
This script generates a string of lowercase English alphabet characters from 'a' to 'z', excluding 'q' and 'e', and prints the result without spaces or newlines.

Modules:
    None

Functions:
    None

Variables:
    chars (str): A string containing the lowercase English alphabet characters from 'a' to 'z', excluding 'q' and 'e'.

Usage:
    Run the script directly to see the output.

Example:
    $ ./script.py
    abcdfghijklmnopqrstuvwxyz
"""

# Generate a string of lowercase letters from 'a' to 'z', excluding 'q' and 'e'
chars = ''.join(
    chr(i) for i in range(97, 123) if chr(i) not in {'q', 'e'}
)

# Print the resulting string without a newline
print('{}'.format(chars), end='')
