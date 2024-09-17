class BankAccount:
    def __init__(self, user, balance=0):
        self.user = user
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Added {amount} to the balance. New balance is {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "insufficient fund"
        else:
            self.balance -= amount
            return f"Withdraw {amount}. New balance is {self.balance}"

account = BankAccount("Flavio", 15000)

print(account.deposit(50))
print(account.withdraw(150))
print(account.withdraw(200))