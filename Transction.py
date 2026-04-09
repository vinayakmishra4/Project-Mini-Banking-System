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

def transaction_history(account_number, history):
    print(f"Transaction History for account {account_number}:")
    for transaction in history:
        print(transaction)

def  trasnctionmenu(account_number, balance, history):
    while True:
        print("\nTransaction Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            balance = deposit(account_number, amount, balance)
            history.append(f"Deposited ₹{amount}")

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            balance = withdraw(account_number, amount, balance)
            history.append(f"Withdrew ₹{amount}")

        elif choice == "3":
            target_account = input("Enter target account number: ")
            amount = float(input("Enter transfer amount: "))
            balance = transfer(account_number, target_account, amount, balance)
            history.append(f"Transferred ₹{amount} to {target_account}")

        elif choice == "4":
            transaction_history(account_number, history)

        elif choice == "5":
            print("Exiting transaction menu...")
            break

        else:
            print("Invalid choice! Please try again.")
