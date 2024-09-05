#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
print()

uppercase("best")
uppercase("Best School 98 Battery street")
uppercase("holberton")
uppercase("Holberton School, 98 battery street")
uppercase("")
uppercase("z")