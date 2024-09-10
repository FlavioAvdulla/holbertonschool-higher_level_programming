#!/usr/bin/python3
"""
This script demonstrates importing a function from another module and using it to return the length of a string and its first character.

The script imports the `multiple_returns` function from the module named '8-multiple_returns'.
It then defines a sentence and uses the imported function to get the length of the sentence and its first character.
Finally, it prints the length and the first character in a formatted string.

Example:
    $ ./import_and_multiple_returns.py
    Length: 21 - First character: A
"""

multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
