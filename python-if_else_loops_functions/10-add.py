#!/usr/bin/python3
# 10-add.py
def add(a, b):
    # Convert non-integer values to 0
    if type(a) is not int:
        a = 0
    if type(b) is not int:
        b = 0
    return a + b

# 10-main.py
#!/usr/bin/env python3
add = __import__('10-add').add

print(add(1, 2))           # Outputs: 3
print(add(98, 0))          # Outputs: 98
print(add(100, -2))        # Outputs: 98
print(add(-100, -2))       # Outputs: -102
print(add(0, 0))           # Outputs: 
