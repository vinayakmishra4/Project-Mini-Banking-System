# ------------------------------------------------------------
# Account Module
# Handles: account number generation, account creation,
#          card PIN setup, and viewing account details.
# ------------------------------------------------------------

import random
import os
import pandas as pd

# All Excel data files now live in the data/ folder instead of
# cluttering the project root.
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
DETAILS_FILE = os.path.join(DATA_DIR, "details.xlsx")
PIN_FILE = os.path.join(DATA_DIR, "pin.xlsx")


def generate_account_number():
    """Generate a random 10-digit account number (as a string)."""
    # randint ensures a 10-digit number between given range
    # converted to string so it can be safely stored in Excel
    return str(random.randint(1000000000, 9999999999))


def create_account(account_number, name, dob, address, phone, email, balance):
    """Create a new bank account and save details in Excel."""
    print("Creating a new account...")

    account = {
        "account_number": account_number,
        "name": name,
        "dob": dob,
        "address": address,
        "phone": phone,
        "email": email,
        "balance": balance,
    }

    os.makedirs(DATA_DIR, exist_ok=True)

    # If file already exists, load it; otherwise create empty structure
    if os.path.exists(DETAILS_FILE):
        df = pd.read_excel(DETAILS_FILE)
    else:
        df = pd.DataFrame(columns=[
            "account_number", "name", "dob",
            "address", "phone", "email", "balance"
        ])

    # Add new account as a new row
    df = pd.concat([df, pd.DataFrame([account])], ignore_index=True)

    # Save updated data back to Excel
    df.to_excel(DETAILS_FILE, index=False)
    print(f"Account {account_number} created successfully!")
    return account


def cardpin(account_number):
    """Set or update a 4-digit PIN for an account."""
    print("Setting up card PIN...")

    pin = input("Enter a 4-digit PIN: ")

    # Validate PIN: must be exactly 4 digits and numeric
    while len(pin) != 4 or not pin.isdigit():
        print("Invalid PIN. Please enter a 4-digit number.")
        pin = input("Enter a 4-digit PIN: ")

    os.makedirs(DATA_DIR, exist_ok=True)

    if os.path.exists(PIN_FILE):
        df_pin = pd.read_excel(PIN_FILE)
    else:
        df_pin = pd.DataFrame(columns=["account_number", "pin"])

    # Remove old PIN if account already exists (update case)
    df_pin = df_pin[df_pin["account_number"] != account_number]

    # Add new PIN entry
    df_pin = pd.concat(
        [df_pin, pd.DataFrame([{"account_number": account_number, "pin": pin}])],
        ignore_index=True
    )

    df_pin.to_excel(PIN_FILE, index=False)
    print(f"PIN for account {account_number} set successfully!")
    return pin


def view_account_details(account_number):
    """Display stored details of a specific account."""
    print("Viewing account details...")

    if os.path.exists(DETAILS_FILE):
        df = pd.read_excel(DETAILS_FILE, dtype={"account_number": str})
        df["account_number"] = df["account_number"].str.strip()
        account_number = str(account_number).strip()

        account_details = df[df["account_number"] == account_number]

        if not account_details.empty:
            print(account_details.to_string(index=True))
        else:
            print(f"No account found with number {account_number}.")
    else:
        print("No accounts found. Please create an account first.")
