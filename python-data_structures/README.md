# Python List and String Manipulation Tasks

This repository contains a series of Python functions for manipulating lists and strings. Each task is implemented in a separate Python file.

## Table of Contents

1. Print a List of Integers
2. Secure Access to an Element in a List
3. Replace Element
4. Print a List of Integers in Reverse
5. Replace in a Copy
6. Remove Characters 'c' and 'C'
7. Print a Matrix of Integers
8. Tuples Addition
9. More Returns
10. Find the Max
11. Only by 2
12. Delete at
13. Switch

## Print a List of Integers

**File:** [0-print_list_integer.py](0-print_list_integer.py)

Write a function that prints all integers of a list.

- **Prototype:** `def print_list_integer(my_list=[]):`
- **Format:** One integer per line.
- **Constraints:**
  - You are not allowed to import any module.
  - You can assume that the list only contains integers.
  - You are not allowed to cast integers into strings.
  - You have to use `str.format()` to print integers.

## Secure Access to an Element in a List

**File:** [1-element_at.py](1-element_at.py)

Write a function that retrieves an element from a list.

- **Prototype:** `def element_at(my_list, idx):`
- **Constraints:**
  - If `idx` is negative, the function should return `None`.
  - If `idx` is out of range (greater than the number of elements in `my_list`), the function should return `None`.
  - You are not allowed to import any module.
  - You are not allowed to use `try/except`.

## Replace Element

**File:** [2-replace_in_list.py](2-replace_in_list.py)

Write a function that replaces an element of a list at a specific position.

- **Prototype:** `def replace_in_list(my_list, idx, element):`
- **Constraints:**
  - If `idx` is negative, the function should not modify anything and return the original list.
  - If `idx` is out of range (greater than the number of elements in `my_list`), the function should not modify anything and return the original list.
  - You are not allowed to import any module.
  - You are not allowed to use `try/except`.

## Print a List of Integers in Reverse

**File:** [3-print_reversed_list_integer.py](3-print_reversed_list_integer.py)

Write a function that prints all integers of a list, in reverse order.

- **Prototype:** `def print_reversed_list_integer(my_list=[]):`
- **Format:** One integer per line.
- **Constraints:**
  - You are not allowed to import any module.
  - You can assume that the list only contains integers.
  - You are not allowed to cast integers into strings.
  - You have to use `str.format()` to print integers.

## Replace in a Copy

**File:** [4-new_in_list.py](4-new_in_list.py)

Write a function that replaces an element in a list at a specific position without modifying the original list.

- **Prototype:** `def new_in_list(my_list, idx, element):`
- **Constraints:**
  - If `idx` is negative, the function should return a copy of the original list.
  - If `idx` is out of range (greater than the number of elements in `my_list`), the function should return a copy of the original list.
  - You are not allowed to import any module.
  - You are not allowed to use `try/except`.

## Remove Characters 'c' and 'C'

**File:** [5-no_c.py](5-no_c.py)

Write a function that removes all characters 'c' and 'C' from a string.

- **Prototype:** [Click Here](def no_c(my_string):)
- **Constraints:**
  - The function should return the new string.
  - You are not allowed to import any module.
  - You are not allowed to use `str.replace()`.

## Print a Matrix of Integers

**File:** [6-print_matrix_integer.py](6-print_matrix_integer.py)

Write a function that prints a matrix of integers.

- **Prototype:** `def print_matrix_integer(matrix=[[]]):`
- **Format:** See example.
- **Constraints:**
  - You are not allowed to import any module.
  - You can assume that the list only contains integers.
  - You are not allowed to cast integers into strings.
  - You have to use `str.format()` to print integers.

## Tuples Addition

**File:** [7-add_tuple.py](7-add_tuple.py)

Write a function that adds 2 tuples.

- **Prototype:** `def add_tuple(tuple_a=(), tuple_b=()):`
- **Returns:** A tuple with 2 integers:
  - The first element should be the addition of the first element of each argument.
  - The second element should be the addition of the second element of each argument.
- **Constraints:**
  - You are not allowed to import any module.
  - You can assume that the two tuples will only contain integers.
  - If a tuple is smaller than 2, use the value 0 for each missing integer.
  - If a tuple is bigger than 2, use only the first 2 integers.

## More Returns

**File:** [8-multiple_returns.py](8-multiple_returns.py)

Write a function that returns a tuple with the length of a string and its first character.

- **Prototype:** `def multiple_returns(sentence):`
- **Constraints:**
  - If the sentence is empty, the first character should be equal to `None`.
  - You are not allowed to import any module.

## Find the Max

**File:** [9-max_integer.py](9-max_integer.py)

Write a function that finds the biggest integer of a list.

- **Prototype:** `def max_integer(my_list=[]):`
- **Constraints:**
  - If the list is empty, return `None`.
  - You can assume that the list only contains integers.
  - You are not allowed to import any module.
  - You are not allowed to use the builtin `max()`.

## Only by 2

**File:** [10-divisible_by_2.py](10-divisible_by_2.py)

Write a function that finds all multiples of 2 in a list.

- **Prototype:** `def divisible_by_2(my_list=[]):`
- **Returns:** A new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2.
- **Constraints:**
  - The new list should have the same size as the original list.
  - You are not allowed to import any module.

## Delete at

**File:** [11-delete_at.py](11-delete_at.py)

Write a function that deletes the item at a specific position in a list.

- **Prototype:** `def delete_at(my_list=[], idx=0):`
- **Constraints:**
  - If `idx` is negative or out of range, nothing changes (returns the same list).
  - You are not allowed to use `pop()`.
  - You are not allowed to import any module.

## Switch

**File:** [12-switch.py](12-switch.py)

Complete the source code in order to switch the value of `a` and `b`.

- **Source Code:** You can find the source code here.
- **Instructions:** Your code should be inserted where the comment is (line 4).
- **Constraints:**
  - Your program should be exactly 5 lines long.
