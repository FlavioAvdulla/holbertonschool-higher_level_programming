#!/usr/bin/python3
"""
This script demonstrates importing a function from another module and using it to add two tuples element-wise.

The script imports the `add_tuple` function from the module named '7-add_tuple'.
It then creates two tuples and uses the imported function to add them element-wise.
Finally, it prints the resulting tuples after performing the addition.

Example:
    $ ./import_and_add_tuples.py
    (89, 100)
    (2, 89)
    (1, 89)
"""

add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
