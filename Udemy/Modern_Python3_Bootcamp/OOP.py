# Exercises

# 1. Define a new class to register a user to a bank with a starting
#    balance of 0. Deposit and withdraw methods should be available.


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        print(f"Account opened for {owner} with a starting balance of £{balance}.")

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance


new_account = BankAccount("Brandan")
new_account.deposit(126.80)  # balance = balance + 126.80
print(f"Current account balance is £{round(new_account.get_balance(), 2)}.")
