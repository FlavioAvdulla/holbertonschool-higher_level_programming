#!/usr/bin/python3
"""
This script generates a random integer between -10 and 10 and prints whether the number is positive, negative, or zero.

Modules:
    random: This module implements pseudo-random number generators for various distributions.

Variables:
    number (int): A randomly generated integer between -10 and 10.

Functions:
    None

Execution:
    The script performs the following steps:
    1. Generates a random integer between -10 and 10.
    2. Checks if the number is positive, negative, or zero.
    3. Prints a message indicating whether the number is positive, negative, or zero.
"""

import random

number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
elif number == 0:
    print(f"{number} is zero")
