class Bank_Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if not isinstance(amount, int):
            raise TypeError ("You should type only numbers")
        self.balance += amount
        return f"The added amount is: {amount}, new balance is {self.balance}."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient fund."
        else:
            self.balance -= amount
            return f"You withdrew {amount}, your new balance is: {self.balance}"
        print()
account = Bank_Account("Flavio", 1400)

print(account.deposit(80))
print(account.withdraw(2000))
