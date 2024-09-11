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


# def filter_even_numbers(numbers):
#     even_numbers = []
#     for x in numbers:
#         if x in numbers:
#             if x % 2 == 0:
#                 even_numbers.append(x)
#     return even_numbers

# def filter_even_numbers_lc(numbers):
#     return["Even" if x % 2 == 0 else "Odd" for x in numbers]

# print(filter_even_numbers([1, 2, 3, 4, 5]))
# print(filter_even_numbers_lc([1, 2, 3, 4, 5]))


# def filter_palindromic_words(words):
#     palindromic_words = []
#     for word in words:
#         if word == word[::-1]:
#             palindromic_words.append(word)
#     return palindromic_words

# def filter_palindromic_words_lc(words):
#     return [word for word in words if word == word[::-1]]

# print(filter_palindromic_words(["adam", "madam", "dam"]))
# print(filter_palindromic_words_lc(["adam", "madam", "dam"]))


# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1 | set2
# print(union_set)


# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1 & set2
# print(union_set)


# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1 - set2
# print(union_set)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1 ^ set2
# print(union_set)


# my_dict = {
# "name": "Alice",
# "Age": 25,
# "City": "Lushnjë"
# }

# del my_dict["Age"]
# print(my_dict)


my_dict = {
"name": "Alice",
"Age": 25,
"City": "Lushnjë"
}

keys_list = list(my_dict.keys())
values_list = list(my_dict.values())

print(f"Keys:{keys_list}")
print(f"Values:{values_list}")