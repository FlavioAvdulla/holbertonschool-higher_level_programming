# Python Import and Function Projects

This repository contains several Python scripts that demonstrate importing functions from different files and performing various operations. Each script is designed to fulfill specific requirements as outlined below.

## Table of Contents
1. Import a Simple Function
2. My First Toolbox
3. How to Make a Script Dynamic
4. Infinite Addition
5. Who Are You?
6. Everything Can Be Imported

## Import a Simple Function
**0-add.py:** `0-add.py`

This script imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

### Requirements:
- Use the `print` function with string format to display integers.
- Assign the value `1` to a variable called `a`.
- Assign the value `2` to a variable called `b`.
- Use these two variables as arguments when calling the functions `add` and `print`.
- `a` and `b` must be defined in 2 different lines: `a = 1` and `b = 2`.
- The program should print: `<a value> + <b value> = <add(a, b) value>` followed by a new line.
- Only use the word `add_0` once in your code.
- Do not use `*` for importing or `__import__`.
- The code should not be executed when imported.

## My First Toolbox
**1-calculation.py:** `1-calculation.py`

This script imports functions from the file `calculator_1.py`, performs some mathematical operations, and prints the results.

### Requirements:
- Do not use the `print` function (with string format to display integers) more than 4 times.
- Assign the value `10` to a variable `a`.
- Assign the value `5` to a variable `b`.
- Use these two variables only as arguments when calling functions (including `print`).
- `a` and `b` must be defined in 2 different lines: `a = 10` and `b = 5`.
- The script should call each of the imported functions.
- Only use the word `calculator_1` once in your file.
- Do not use `*` for importing or `__import__`.
- The code should not be executed when imported.

## How to Make a Script Dynamic
**2-args.py:** `2-args.py`

This script prints the number of and the list of its arguments.

### Requirements:
- The output should be:
  - `Number of argument(s)` followed by `argument` (if the number is one) or `arguments` (otherwise), followed by `:` (or `.` if no arguments were passed), followed by a new line.
  - If at least one argument is passed, print one line per argument: the position of the argument (starting at 1) followed by `:`, followed by the argument value and a new line.
- The code should not be executed when imported.
- The number of elements of `argv` can be retrieved by using: `len(argv)`.

## Infinite Addition
**3-infinite_add.py:** `3-infinite_add.py`

This script prints the result of the addition of all arguments.

### Requirements:
- The output should be the result of the addition of all arguments, followed by a new line.
- You can cast arguments into integers by using `int()` (you can assume that all arguments can be cast into integers).
- The code should not be executed when imported.

## Who Are You?
**4-hidden_discovery.py:** `4-hidden_discovery.py`

This script prints all the names defined by the compiled module `hidden_4.pyc`.

### Requirements:
- This task must be done on the sandbox only.
- The file `4-hidden_discovery.py` must be located in the folder `/tmp/`.
- Print one name per line, in alphabetical order.
- Print only names that do not start with `__`.
- The code should not be executed when imported.

## Everything Can Be Imported
**5-variable_load.py:** `5-variable_load.py`

This script imports the variable `a` from the file `variable_load_5.py` and prints its value.

### Requirements:
- Do not use `*` for importing or `__import__`.
- The code should not be executed when imported.