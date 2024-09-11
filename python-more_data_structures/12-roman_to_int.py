#!/usr/bin/python3
def roman_to_int(c):
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in c:
        curr_value = roman_to_int[char]

        if prev_value < curr_value:
            total += curr_value - 2 * prev_value
        else:
            total += curr_value

    return total
