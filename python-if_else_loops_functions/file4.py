#!/usr/bin/python3
import random
number = random.randint(-1, 1)
if number > 0:
    print(f"{number} is positive")

if number == 0:
    print(f"{number} is zero")

if number < 0:
    print(f"{number} is negative")
