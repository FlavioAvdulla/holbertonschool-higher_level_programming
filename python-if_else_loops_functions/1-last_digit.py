#!/usr/bin/python3
"""
This script generates a random integer between -10,000 and 10,000, calculates its last digit, and prints a message based on the value of the last digit.

Modules:
    random: This module implements pseudo-random number generators for various distributions.

Functions:
    None

Variables:
    text (str): A string used in the output message.
    number (int): A random integer between -10,000 and 10,000.
    last_digit (int): The last digit of the absolute value of the number.

Usage:
    Run the script directly to see the output.

Example:
    $ ./script.py
    Last digit of -1234 is 4 and is less than 6 and not 0
"""

import random

# Define the text to be used in the output message
text = 'Last digit of'

# Generate a random integer between -10,000 and 10,000
number = random.randint(-10000, 10000)

# Calculate the last digit of the absolute value of the number
last_digit = abs(number) % 10

# Adjust the last digit if the number is negative
if number < 0:
    last_digit = last_digit * -1

# Print the appropriate message based on the value of the last digit
if last_digit > 5:
    print(f"{text} {number} is {last_digit} and is greater than 5")

if last_digit == 0:
    print(f"{text} {number} is {last_digit} and is 0")

if last_digit != 0 and last_digit < 6:
    print(f"{text} {number} is {last_digit} and is less than 6 and not 0")
