#!/usr/bin/python3
import random

"""
Script Documentation

Overview:
This Python script generates a random integer between -10,000 and 10,000, calculates its last digit, and prints a message based on the value of the last digit.

Modules Used:
- random: This module is used to generate random numbers.

Variables:
- text: A string that is part of the message to be printed.
- number: A randomly generated integer between -10,000 and 10,000.
- last_digit: The last digit of the absolute value of 'number'.

Logic:
1. Generate a Random Number:
   number = random.randint(-10000, 10000)
   This line generates a random integer between -10,000 and 10,000.

2. Calculate the Last Digit:
   last_digit = abs(number) % 10
   This line calculates the last digit of the absolute value of 'number'.

3. Adjust Last Digit for Negative Numbers:
   if number < 0:
       last_digit = last_digit * -1
   If the original number is negative, the last digit is made negative.

4. Print Messages Based on Last Digit:
   - If the last digit is greater than 5:
     if last_digit > 5:
         print(f"{text} {number} is {last_digit} and is greater than 5")
   - If the last digit is 0:
     if last_digit == 0:
         print(f"{text} {number} is {last_digit} and is 0")
   - If the last digit is less than 6 and not 0:
     if last_digit != 0 and last_digit < 6:
         print(f"{text} {number} is {last_digit} and is less than 6 and not 0")
"""

# A string that is part of the message to be printed
text = 'Last digit of'

# Generate a random integer between -10,000 and 10,000
number = random.randint(-10000, 10000)

# Calculate the last digit of the absolute value of 'number'
last_digit = abs(number) % 10

# If the original number is negative, make the last digit negative
if number < 0:
    last_digit = last_digit * -1

# Print messages based on the value of the last digit
if last_digit > 5:
    print(f"{text} {number} is {last_digit} and is greater than 5")

if last_digit == 0:
    print(f"{text} {number} is {last_digit} and is 0")

if last_digit != 0 and last_digit < 6:
    print(f"{text} {number} is {last_digit} and is less than 6 and not 0")
