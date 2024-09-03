# Enter Calculation: 5 * 6
# 5 * 6 = 30

# Store the user input of 2 numbers and the operator
num1, operator, num2 = input('Enter Calculation ').split()

# Convert the string into integers
num1 = int(num1)
num2 = int(num2)

# If + then we need to provide output based on addition
# Print the result
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))

elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))

elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))

elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
	print("Use either + - * / next time")