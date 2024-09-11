#!/usr/bin/python3
""" 
Roman to Integer test file

Overview:
This script tests the `roman_to_int` function from the `12-roman_to_int` module. It converts various Roman numerals to their integer equivalents and prints the results.

Modules Used:
- 12-roman_to_int: This module contains the `roman_to_int` function.

Variables:
- roman_number: A string representing a Roman numeral.

Functions:
- roman_to_int(roman_number): Converts a Roman numeral to its integer equivalent.

Logic:
1. Import the `roman_to_int` function from the `12-roman_to_int` module.
2. Define various Roman numeral strings.
3. Call the `roman_to_int` function with each Roman numeral and print the result.
"""

roman_to_int = __import__('12-roman_to_int').roman_to_int

# Define and convert various Roman numerals to integers
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
