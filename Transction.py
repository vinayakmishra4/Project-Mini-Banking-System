# Simple Banking System

# Account class
class Account:
    def __init__(self, account, balance=0):
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


# Transaction menu
def transaction_menu(account):
    while True:
        print("\n--- Transaction Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                deposit(account, amount)
            except ValueError:
                print("Please enter a valid number")

        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                withdraw(account, amount)
            except ValueError:
                print("Please enter a valid number")

        elif choice == '3':
            print(f"Current balance: {account.balance}")

        elif choice == '4':
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Try again.")
