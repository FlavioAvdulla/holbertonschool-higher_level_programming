#!/usr/bin/python3
string = input('Float:')
try:
	number = float(string)
	if number > 0:
		print("{:.2f}\n".format(number))
		print("Correct Output - positive")
	elif number < 0:
		print("{:.2f}\n".format(number))
		print("Correct Output - negative")
	else:
		print("{:.2f}\n".format(number))
		print("Correct Output - zero")
except ValueError:
	printf("Correct Output - wrong type")
