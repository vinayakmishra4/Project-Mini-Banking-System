# Project Mini Banking System

import Account as ac
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