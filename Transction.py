# Simple Banking System with Transaction History

# Account class
class Account:
    def __init__(self, account, balance=0):
        self.account_number = account
        self.balance = balance
        self.history = []   # store transaction history


# Deposit function
def deposit(account, amount):
    if amount > 0:
        account.balance += amount
        account.history.append(f"Deposited {amount}")
        print(f"Deposited {amount}. New balance: {account.balance}")
    else:
        print("Invalid deposit amount")


# Withdrawal function
def withdraw(account, amount):
    if amount <= 0:
        print("Invalid withdrawal amount")
    elif account.balance >= amount:
        account.balance -= amount
        account.history.append(f"Withdrew {amount}")
        print(f"Withdrew {amount}. New balance: {account.balance}")
    else:
        print("Insufficient funds")


# Show transaction history
def show_history(account):
    print("\n--- Transaction History ---")
    if not account.history:
        print("No transactions yet.")
    else:
        for i, record in enumerate(account.history, start=1):
            print(f"{i}. {record}")


# Transaction menu
def transaction_menu(account):
    while True:
        print("\n--- Transaction Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

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
            show_history(account)

        elif choice == '5':
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


# Main program
def main():
    account_number = input("Enter account number: ")
    user_account = Account(account_number, 0)

    print(f"\nAccount created successfully! Account No: {account_number}")
    transaction_menu(user_account)


# Run program
if __name__ == "__main__":
    main()