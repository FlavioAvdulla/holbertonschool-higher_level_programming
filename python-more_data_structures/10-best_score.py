#!/usr/bin/python3

"""
Script Documentation

Overview:
This Python script defines a function `best_score` that returns the key with the highest integer value from a given dictionary. If the dictionary is empty or `None`, the function returns `None`.

Function:
- best_score(a_dictionary):
    - Parameters:
        - a_dictionary: A dictionary where keys are strings and values are integers.
    - Returns:
        - The key with the highest integer value.
        - `None` if the dictionary is empty or `None`.

Logic:
1. Check if the dictionary is empty or `None`. If so, return `None`.
2. Initialize `best_key` and `best_value` to `None`.
3. Iterate through each key-value pair in the dictionary.
4. If `best_value` is `None` or the current value is greater than `best_value`, update `best_value` and `best_key`.
5. Return `best_key`.
"""

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    best_value = None

    for key, value in a_dictionary.items():
        if best_value is None or value > best_value:
            best_value = value
            best_key = key

    return best_key
