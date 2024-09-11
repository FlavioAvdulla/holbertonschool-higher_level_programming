#!/usr/bin/python3

"""
Script Documentation

Overview:
This Python script imports the `best_score` function from the `10-best_score` module and uses it to find the key with the highest integer value in a given dictionary. It then prints the result. The script also handles the case where the input dictionary is `None`.

Modules Used:
- 10-best_score: This module contains the `best_score` function.

Variables:
- a_dictionary: A dictionary with keys as names (strings) and values as scores (integers).
- best_key: The key with the highest score returned by the `best_score` function.

Functions:
- best_score(a_dictionary): Returns the key with the highest integer value from the given dictionary.

Logic:
1. Import the `best_score` function from the `10-best_score` module.
2. Define a dictionary `a_dictionary` with sample data.
3. Call the `best_score` function with `a_dictionary` and print the result.
4. Call the `best_score` function with `None` and print the result.
"""

best_score = __import__('10-best_score').best_score

# Define a dictionary with sample data
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}

# Find and print the key with the highest score
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

# Handle the case where the input dictionary is None
best_key = best_score(None)
print("Best score: {}".format(best_key))
