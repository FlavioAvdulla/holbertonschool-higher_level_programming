#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += "{:c}".format(ord(char) - 32)
        else:
            result += "{:c}".format(ord(char))
    print(result)

uppercase("best")
uppercase("Best School 98 Battery street")