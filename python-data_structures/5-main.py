#!/usr/bin/python3
"""
This script demonstrates importing a function from another module and using it to remove all occurrences of the characters 'c' and 'C' from strings.

The script imports the `no_c` function from the module named '5-no_c'.
It then uses the imported function to remove 'c' and 'C' from several example strings and prints the results.

Example:
    $ ./import_and_remove_c.py
    Best Shool
    hicago
    is fun!
"""

no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
