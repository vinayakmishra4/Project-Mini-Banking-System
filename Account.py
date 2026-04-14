# importing necessary libraries
import random
import pandas as pd
import os


# ------------------------------------------------------------
# Function: generate_account_number
# Purpose : Generate a random 10-digit account number
# ------------------------------------------------------------
def generate_account_number():
    # randint ensures a 10-digit number between given range
    # converted to string so it can be safely stored in Excel
    return str(random.randint(1000000000, 9999999999))


# ------------------------------------------------------------
# Function: create_account
# Purpose : Create a new bank account and save details in Excel
# ------------------------------------------------------------
def create_account(account_number, name, dob, address, phone, email, balance):
    print("Creating a new account...")

    # Store all user inputs in a dictionary (one record)
    account = {
        "account_number": account_number,
        "name": name,
        "dob": dob,
        "address": address,
        "phone": phone,
        "email": email,
        "balance": balance,
    }

    # Excel file where all account records are stored
    file_name = "details.xlsx"

    # If file already exists, load it; otherwise create empty structure
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
    else:
        df = pd.DataFrame(columns=[
            "account_number", "name", "dob",
            "address", "phone", "email", "balance"
        ])

    # Add new account as a new row
    df = pd.concat([df, pd.DataFrame([account])], ignore_index=True)

    # Save updated data back to Excel
    df.to_excel(file_name, index=False)

    print(f"Account {account_number} created successfully!")
    return account


# ------------------------------------------------------------
# Function: cardpin
# Purpose : Set or update a 4-digit PIN for an account
# ------------------------------------------------------------
def cardpin(account_number):
    print("Setting up card PIN...")

    # Take PIN input from user
    pin = input("Enter a 4-digit PIN: ")

    # Validate PIN: must be exactly 4 digits and numeric
    while len(pin) != 4 or not pin.isdigit():
        print("Invalid PIN. Please enter a 4-digit number.")
        pin = input("Enter a 4-digit PIN: ")

    # File where PINs are stored
    pin_file = "pin.xlsx"

    # Load existing PIN data or create new structure
    if os.path.exists(pin_file):
        df_pin = pd.read_excel(pin_file)
    else:
        df_pin = pd.DataFrame(columns=["account_number", "pin"])

    # Remove old PIN if account already exists (update case)
    df_pin = df_pin[df_pin["account_number"] != account_number]

    # Add new PIN entry
    df_pin = pd.concat(
        [df_pin, pd.DataFrame([{"account_number": account_number, "pin": pin}])],
        ignore_index=True
    )

    # Save updated PIN data
    df_pin.to_excel(pin_file, index=False)

    print(f"PIN for account {account_number} set successfully!")
    return pin


# ------------------------------------------------------------
# Function: view_account_details
# Purpose : Display stored details of a specific account
# ------------------------------------------------------------
def view_account_details(account_number):
    print("Viewing account details...")

    file_name = "details.xlsx"

    # Check if account database exists
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)

        # Filter rows matching the given account number
        account_details = df[df["account_number"] == account_number]

        # If account exists, display it
        if not account_details.empty:
            print(account_details.to_string(index=False))
        else:
            print(f"No account found with number {account_number}.")
    else:
        print("No accounts found. Please create an account first.")