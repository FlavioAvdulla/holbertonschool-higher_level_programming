#!/usr/bin/python3
for n in range(100):
    if n < 99:
        print("{}, ".format(n), end='')
    else:
        print("{}".format(n), end='')
