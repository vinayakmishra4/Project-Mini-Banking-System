# Project Mini Banking System

import Account as ac
import Transction as tc
class Account:
    def __init__(self, name, dob, address, phone, email, balance):
        self.name = name
        self.dob = dob
        self.address = address
        self.phone = phone
        self.email = email
        self.balance = balance
        self.account_number = ac.generate_account_number()
        self.pin = ac.cardpin(self.account_number)
    def create_account(self):
        account_details = ac.create_account(self.account_number, self.name, self.dob, self.address, self.phone, self.email, self.balance)
        return account_details

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        new_balance = tc.deposit(self.account_number, amount)
        if new_balance is None:
            raise Exception("Deposit failed")
        self.balance = new_balance
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        new_balance = tc.withdraw(self.account_number, amount, self.balance)
        if new_balance is None:
            raise Exception("Withdrawal failed")
        self.balance = new_balance
        return self.balance

    def transfer(self, target_account, amount):
        self.balance = tc.transfer(self.account_number, target_account, amount, self.balance)
        return self.balance
# Example usage
if __name__ == "__main__":  
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    balance = float(input("Enter your initial balance: "))

    new_account = Account(name, dob, address, phone, email, balance)
    account_details = new_account.create_account()
    print("Account created successfully!")
    print(account_details)

    while True:
        print("\nChoose Transaction:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            new_balance = new_account.deposit(amount)
            print("Updated Balance:", new_balance)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            new_balance = new_account.withdraw(amount)
            print("Updated Balance:", new_balance)

        elif choice == "3":
            target_account = input("Enter target account number: ")
            amount = float(input("Enter amount to transfer: "))
            new_balance = new_account.transfer(target_account, amount)
            print("Updated Balance:", new_balance)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")