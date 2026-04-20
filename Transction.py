# Transaction class for handling banking transactions
import Account as ac
file='details.json'

account=ac.generate_account_number()

# Account class
class Account:
    def __init__(self, account , balance):
        self.account_number = account
        self.balance = balance


# Deposit function
def deposit(account, amount):
    if amount > 0:
        account.balance += amount
        print(f"Deposited {amount}. New balance: {account.balance}")
    else:
        print("Invalid deposit amount")


# Withdrawal function
def withdraw(account, amount):
    if amount <= 0:
        print("Invalid withdrawal amount")
    elif account.balance >= amount:
        account.balance -= amount
        print(f"Withdrew {amount}. New balance: {account.balance}")
    else:
        print("Insufficient funds") 