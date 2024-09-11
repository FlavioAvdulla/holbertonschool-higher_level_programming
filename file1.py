# def square_numbers(numbers):
#     squared_numbers = []
#     for x in numbers:
#         squared_numbers.append(x**2)
#     return squared_numbers

# def square_numbers_lc(numbers):
#     return [x**2 for x in numbers]

# print(square_numbers([1, 4, 2, 6, 7]))
# print(square_numbers_lc([1, 4, 2, 6, 7]))


# def uppercase_names(names):
#     uppercase_names = []
#     for name in names:
#         uppercase_names.append(name.upper())
#     return uppercase_names

# def uppercase_names_lc(names):
#     return [name.upper() for name in names]

# print(uppercase_names(["John", "James", "Alice"]))
# print(uppercase_names_lc(["John", "James", "Alice"]))


def filter_even_numbers(numbers):
    even_numbers = []
    for x in numbers:
        if x in numbers:
            if x % 2 == 0:
                even_numbers.append(x)
    return even_numbers

def filter_even_numbers_lc(numbers):
    return["Even" if x % 2 == 0 else "Odd" for x in numbers ]

print(filter_even_numbers([1, 2, 3, 4, 5]))
print(filter_even_numbers_lc([1, 2, 3, 4, 5]))