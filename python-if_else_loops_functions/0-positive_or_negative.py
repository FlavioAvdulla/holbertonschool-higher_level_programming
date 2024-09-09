#!/usr/bin/python3
"""
This script generates a random integer between -10 and 10 and prints whether the number is positive, negative, or zero.

Modules:
    random: This module implements pseudo-random number generators for various distributions.

Functions:
    None

Variables:
    number (int): A random integer between -10 and 10.

Usage:
    Run the script directly to see the output.

Example:
    $ ./script.py
    5 is positive
"""

import random

# Generate a random integer between -10 and 10
number = random.randint(-10, 10)

# Check if the number is positive, negative, or zero and print the result
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
elif number == 0:
    print(f"{number} is zero")
