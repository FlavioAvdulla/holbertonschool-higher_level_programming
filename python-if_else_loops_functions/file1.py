num1, operator, num2 = input("Enter your calculations: ").split()

num1 = int(num1)
num2 = int(num2)

if operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

elif operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
    
else:
    print("Invalid output. :(")