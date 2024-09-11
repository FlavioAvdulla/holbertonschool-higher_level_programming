#!/usr/bin/python3

"""
Script Documentation

Overview:
This Python script defines a function `roman_to_int` that converts a Roman numeral string to its integer equivalent. The function handles both valid and invalid inputs gracefully.

Function:
- roman_to_int(roman_string):
    - Parameters:
        - roman_string: A string representing a Roman numeral.
    - Returns:
        - An integer representing the value of the Roman numeral.
        - Returns 0 if the input is not a string or is `None`.

Logic:
1. Check if the input is a valid string. If not, return 0.
2. Define a dictionary `roman_values` that maps Roman numeral characters to their integer values.
3. Initialize `total` to 0 and `prev_value` to 0.
4. Iterate through the characters of the reversed Roman numeral string.
5. For each character, get its integer value from the dictionary.
6. If the current value is less than the previous value, subtract it from `total`. Otherwise, add it to `total`.
7. Update `prev_value` to the current value.
8. Return the `total` as the integer equivalent of the Roman numeral.
"""

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_values.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total
