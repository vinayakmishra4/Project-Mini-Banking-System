# importing necessary libraries
import random
import pandas as pd
import os

# Function to generate a unique 10-digit account number
def generate_account_number():
    return str(random.randint(1000000000, 9999999999))  # String for Excel keys

# Function to create a new account and save to Excel
def create_account(account_number, name, dob, address, phone, email, balance):
    print("Creating a new account...")

    # Create account details dictionary
    account = {
        "account_number": account_number,
        "name": name,
        "dob": dob,
        "address": address,
        "phone": phone,
        "email": email,
        "balance": balance,
    }

    # File to store account details
    file_name = "details.xlsx"

    # Load existing data if Excel file exists
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
    else:
        df = pd.DataFrame(columns=["account_number", "name", "dob", "address", "phone", "email", "balance"])

    # Append new account
    df = pd.concat([df, pd.DataFrame([account])], ignore_index=True)

    # Save back to Excel
    df.to_excel(file_name, index=False)

    print(f"Account {account_number} created successfully!")
    return account

# Function to set up card PIN for the account
def cardpin(account_number):
    print("Setting up card PIN...")

    # Validate PIN input
    pin = input("Enter a 4-digit PIN: ")
    while len(pin) != 4 or not pin.isdigit():
        print("Invalid PIN. Please enter a 4-digit number.")
        pin = input("Enter a 4-digit PIN: ")

    # File to store PINs
    pin_file = "pin.xlsx"

    # Load existing PIN data if file exists
    if os.path.exists(pin_file):
        df_pin = pd.read_excel(pin_file)
    else:
        df_pin = pd.DataFrame(columns=["account_number", "pin"])

    # Update or add the PIN for the account number
    df_pin = df_pin[df_pin["account_number"] != account_number]  # Remove old PIN if exists
    df_pin = pd.concat([df_pin, pd.DataFrame([{"account_number": account_number, "pin": pin}])], ignore_index=True)

    # Save back to Excel
    df_pin.to_excel(pin_file, index=False)

    print(f"PIN for account {account_number} set successfully!")
    return pin

def view_account_details(account_number):
    print("Viewing account details...")

    # File to store account details
    file_name = "details.xlsx"

    # Load existing data if Excel file exists
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
        account_details = df[df["account_number"] == account_number]
        if not account_details.empty:
            print(account_details.to_string(index=False))
        else:
            print(f"No account found with number {account_number}.")
    else:
        print("No accounts found. Please create an account first.")