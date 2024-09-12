# Python Programming Tasks

This repository contains a collection of Python programs designed to perform various tasks. Each task is implemented in a separate Python file.

## Table of Contents

1. Positive Anything is Better than Negative Nothing
2. The Last Digit
3. The Alphabet Game
4. Alphabet Soup
5. Hexadecimal Printing
6. 00...99
7. Inventing is a Combination of Brains and Materials
8. islower
9. To Uppercase
10. There are Only 3 Colors, 10 Digits, and 7 Notes; It's What We Do with Them That's Important
11. a + b
12. a ^ b
13. Fizz Buzz

## Positive Anything is Better than Negative Nothing

**File:** [0-positive_or_negative.py](0-positive_or_negative.py)

This program assigns a random signed number to the variable `number` each time it is executed. It then prints whether the number stored in the variable `number` is positive, negative, or zero.

- The variable `number` will store a different value every time you run this program.
- You don’t have to understand what `import`, `random.randint` do. Please do not touch this code.

**Output:**
- The number, followed by:
  - if the number is greater than 0: `is positive`
  - if the number is 0: `is zero`
  - if the number is less than 0: `is negative`
- Followed by a new line.

## The Last Digit

**File:** [1-last_digit.py](1-last_digit.py)

This program assigns a random signed number to the variable `number` each time it is executed. It then prints the last digit of the number stored in the variable `number`.

- The variable `number` will store a different value every time you run this program.
- You don’t have to understand what `import`, `random.randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000, 10000)`

**Output:**
- The string `Last digit of`, followed by:
  - the number, followed by
  - the string `is`, followed by the last digit of `number`, followed by:
    - if the last digit is greater than 5: the string `and is greater than 5`
    - if the last digit is 0: the string `and is 0`
    - if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
- Followed by a new line.

## The Alphabet Game

**File:** [2-print_alphabet.py](2-print_alphabet.py)

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- Use only one `print` function with string format.
- Use only one loop in your code.
- You are not allowed to store characters in a variable.
- You are not allowed to import any module.

## Alphabet Soup

**File:** [3-print_alphabt.py](3-print_alphabt.py)

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- Print all the letters except `q` and `e`.
- Use only one `print` function with string format.
- Use only one loop in your code.
- You are not allowed to store characters in a variable.
- You are not allowed to import any module.

## Hexadecimal Printing

**File:** [4-print_hexa.py](4-print_hexa.py)

Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal.

- Use only one `print` function with string format.
- Use only one loop in your code.
- You are not allowed to store numbers or strings in a variable.
- You are not allowed to import any module.

## 00...99

**File:** [5-print_comb2.py](5-print_comb2.py)

Write a program that prints numbers from 0 to 99.

- Numbers must be separated by `,`, followed by a space.
- Numbers should be printed in ascending order, with two digits.
- The last number should be followed by a new line.
- Use no more than 2 `print` functions with string format.
- Use only one loop in your code.
- You are not allowed to store numbers or strings in a variable.
- You are not allowed to import any module.

## Inventing is a Combination of Brains and Materials

**File:** [6-print_comb3.py](6-print_comb3.py)

Write a program that prints all possible different combinations of two digits.

- Numbers must be separated by `,`, followed by a space.
- The two digits must be different.
- `01` and `10` are considered the same combination of the two digits `0` and `1`.
- Print only the smallest combination of two digits.
- Numbers should be printed in ascending order, with two digits.
- The last number should be followed by a new line.
- Use no more than 3 `print` functions with string format.
- Use no more than 2 loops in your code.
- You are not allowed to store numbers or strings in a variable.
- You are not allowed to import any module.

## islower

**File:** [7-islower.py](7-islower.py)

Write a function that checks for lowercase character.

- **Prototype:** `def islower(c):`
- Returns `True` if `c` is lowercase.
- Returns `False` otherwise.
- You are not allowed to import any module.
- You are not allowed to use `str.upper()` and `str.isupper()`.
- Tips: `ord()`

## To Uppercase

**File:** [8-uppercase.py](8-uppercase.py)

Write a function that prints a string in uppercase followed by a new line.

- **Prototype:** `def uppercase(str):`
- Use no more than 2 `print` functions with string format.
- Use only one loop in your code.
- You are not allowed to import any module.
- You are not allowed to use `str.upper()` and `str.isupper()`.
- Tips: `ord()`

## There are Only 3 Colors, 10 Digits, and 7 Notes; It's What We Do with Them That's Important

**File:** [9-print_last_digit.py](9-print_last_digit.py)

Write a function that prints the last digit of a number.

- **Prototype:** `def print_last_digit(number):`
- Returns the value of the last digit.
- You are not allowed to import any module.

## a + b

**File:** [10-add.py](10-add.py)

Write a function that adds two integers and returns the result.

- **Prototype:** `def add(a, b):`
- Returns the value of `a + b`.
- You are not allowed to import any module.

## a ^ b

**File:** [11-pow.py](11-pow.py)

Write a function that computes `a` to the power of `b` and returns the value.

- **Prototype:** `def pow(a, b):`
- Returns the value of `a ^ b`.
- You are not allowed to import any module.

## Fizz Buzz

**File:** [12-fizzbuzz.py](12-fizzbuzz.py)

Write a function that prints the numbers from 1 to 100 separated by a space.

- For multiples of three, print `Fizz` instead of the number and for multiples of five, print `Buzz`.
- For numbers which are multiples of both three and five, print `FizzBuzz`.
- **Prototype:** `def fizzbuzz():`
- Each element should be followed by a space.
- You are not allowed to import any module.
