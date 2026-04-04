# Transaction.py
import Account as ac

account_number = ac.generate_account_number()
def deposit(account_number, amount, balance):
    if amount <= 0:
        print("Invalid deposit amount")
        return balance

    balance += amount
    print(f"₹{amount} deposited successfully in account {account_number}")
    return balance


def withdraw(account_number, amount, balance):
    if amount <= 0:
        print("Invalid withdrawal amount")
        return balance

    if balance >= amount:
        balance -= amount
        print(f"₹{amount} withdrawn successfully from account {account_number}")
    else:
        print("Insufficient balance")

    return balance


def transfer(account_number, target_account, amount, balance):
    if amount <= 0:
        print("Invalid transfer amount")
        return balance

    if balance >= amount:
        balance -= amount
        print(f"₹{amount} transferred from {account_number} to {target_account}")
    else:
        print("Insufficient balance")

    return balance