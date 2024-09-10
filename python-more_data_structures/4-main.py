#!/usr/bin/python3
"""
This script demonstrates the use of the `only_diff_elements` function from the `4-only_diff_elements` module.

The `only_diff_elements` function takes two sets and returns a set containing the elements that are unique to each set (i.e., elements that are in either set but not in both).

Functions:
    only_diff_elements(set_1, set_2): Returns a set containing the elements that are unique to each set.

Example:
    The script initializes two sets, `set_1` and `set_2`, with several programming languages. It then calls the `only_diff_elements` function to find the elements that are unique to each set. The result is stored in `od_set`.

    Finally, the script prints the sorted list of unique elements.

Usage:
    Run the script using a Python interpreter.
"""

# Import the only_diff_elements function from the 4-only_diff_elements module
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

# Initialize two sets with several programming languages
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }

# Find the elements that are unique to each set
od_set = only_diff_elements(set_1, set_2)

# Print the sorted list of unique elements
print(sorted(list(od_set)))
