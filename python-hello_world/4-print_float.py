#!/usr/bin/python3
number = 3.14159
string = input('Float:')

try:
    number = float(string)
    if number > 0:
        print("{:.2f}".format(number))
        print("Correct output - positive")
    elif number < 0:
        print("{:.2f}".format(number))
        print("Correct output - negative")
    else:
        print("{:.2f}".format(number))
        print("Correct output - zero")
except ValueError:
    print("Correct output - wrong type")
