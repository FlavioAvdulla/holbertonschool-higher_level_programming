#!/usr/bin/python3
"""
This script runs the fizzbuzz function, which prints the numbers from 1 to 100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz".

Modules:
    None

Functions:
    fizzbuzz(): Prints the numbers from 1 to 100 with the specified replacements.

Usage:
    Run the script directly to see the output.

Example:
    $ ./script.py
    1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 ...
"""

def fizzbuzz():
    """
    Print the numbers from 1 to 100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz".

    Args:
        None

    Returns:
        None
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

if __name__ == "__main__":
    fizzbuzz()
    print("")
