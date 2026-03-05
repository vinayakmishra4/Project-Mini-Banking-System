import random
import json
import os

def generate_account_number():
    return random.randint(1000000000, 9999999999)

account_number = generate_account_number()

def create_account(account_number, name, dob, address, phone, email):
    print("Creating a new account...")

    account = {
        "acc_number": account_number,
        "name": name,
        "dob": dob,
        "address": address,
        "phone": phone,
        "email": email
    }

    file_name = "details.json"

    # Load existing data
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            data = json.load(f)
    else:
        data = []

    # Add new account
    data.append(account)

    # Save back to JSON
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

    print("Account created successfully!")

    return account

def cardpin(account_number):
    print("Setting up card PIN...")

    pin = int(input("Enter a 4-digit PIN: "))

    while len(str(pin)) != 4 or not isinstance(pin, int):
        print("Invalid PIN. Please enter a 4-digit number.")
        pin = int(input("Enter a 4-digit PIN: "))

    file_name = "account_pin.json"

    pin_data = {
        "acc_number": account_number,
        "pin": pin
    }

    # Load existing pins
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(pin_data)

    # Save JSON
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

    print("Card PIN set successfully!")

    return pin