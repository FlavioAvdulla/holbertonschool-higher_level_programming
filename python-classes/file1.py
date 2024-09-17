shopping_list = {
    "Order from Baboon": 5,
    "Molto": 40,
    "Homecooked meal": 3,
    "Dream Job": 2
}

# def add_item(name, quantity):
#     shopping_list[name] = quantity
#     return shopping_list

# def remove_item(name):
#     del shopping_list[name]
#     return shopping_list

# def view_shopping_list():
#     print("Shopping list contains:")
#     print("Item\t\t\t\tQuantity")
#     for key, value in shopping_list.items():
#         print("{:<18} {:18}".format(key, value))
#     print()

# def check_item(name):
#     item = input("Enter the item name you want to check: ")
#     if item in shopping_list:
#         print(f"{item} is in the shopping list.")
#     else:
#         print(f"{item} is not in the shopping list.")
# check_item(shopping_list)

def clear_shopping_list(shopping_list):
    shopping_list.clear()
    print(shopping_list)
    
clear_shopping_list(shopping_list)

# def total_items(shopping_list):
#     total = sum(shopping_list.values())
#     print(f"Total number in the shopping list is: {total}")

# total_items(shopping_list)

# while True:
#     print("1. Add item")
#     print("2. Remove item")
#     print("3. View shopping list")
#     print("4. Exit")
#     choice = int(input("Enter your choice: "))
#     if (choice == 3):
#         view_shopping_list()
#     elif choice == 4:
#         exit 
#     else:
#         print("invalid choice")
