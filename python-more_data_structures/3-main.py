#!/usr/bin/python3
"""
This script demonstrates the use of the `common_elements` function from the `3-common_elements` module.

The `common_elements` function takes two sets and returns a set containing the elements that are common to both sets.

Functions:
    common_elements(set_1, set_2): Returns a set containing the common elements of `set_1` and `set_2`.

Example:
    The script initializes two sets, `set_1` and `set_2`, with several programming languages. It then calls the `common_elements` function to find the common elements between the two sets. The result is stored in `c_set`.

    Finally, the script prints the sorted list of common elements.

Usage:
    Run the script using a Python interpreter.
"""

# Import the common_elements function from the 3-common_elements module
common_elements = __import__('3-common_elements').common_elements

# Initialize two sets with several programming languages
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }

# Find the common elements between the two sets
c_set = common_elements(set_1, set_2)

# Print the sorted list of common elements
print(sorted(list(c_set)))
