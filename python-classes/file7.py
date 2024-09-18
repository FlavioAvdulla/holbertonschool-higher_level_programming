class Check_incomes:
    def __init__(self, name):
        self.__name = name
        self.__incomes = []

    def add_income(self, amount):
        self.__incomes.append(amount)
        return self.__incomes

    def get_incomes(self):
        return self.__incomes


def main():

    person = Check_incomes("Flavio")

    person.add_income(600)
    person.add_income(900)
    person.add_income(1600)
    person.add_income(2600)

    print(f"Name: {person._Check_incomes__name}")
    print(f"Incomes: {person.get_incomes()}")

if __name__ == "__main__":
    main()






# income_list = {
#     "gerti": 400,
#     "stilian": 1500,
#     "flavio": 800,
#     "hans": 1200
# }

# highest_value = max(check_incomes.values())
#     print(highest_value)


# Write a class People that produces this people with a private instance attribute income,adds them to a list,and is fed as an argument to another function along with a person object name
