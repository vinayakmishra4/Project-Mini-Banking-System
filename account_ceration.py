# import the Account module to use its functions for account creation and management
import Account as ac

# Define the Account class to represent a bank account with attributes and methods for account creation
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

# Main function to execute the account creation process by taking user input and creating a new account
if __name__ == "__main__":  
    # Take user input for account details
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    balance = float(input("Enter your initial balance: "))

    # Create a new account using the Account class and print the account details
    new_account = Account(name, dob, address, phone, email, balance)
    account_details = new_account.create_account()
    print("Account created successfully!")
    print(account_details)

    # Print the generated account number and PIN for the user
    
