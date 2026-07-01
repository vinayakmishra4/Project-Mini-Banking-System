# ==============================
# Mini Bank System (Console App)
# ==============================
import os
import sys

# Make sure the project root (this file's folder) is on sys.path so the
# "modules" package can be found no matter where mbs.py is run from
# (double-clicked, run from another directory, run inside an IDE, etc.)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importing required functions from the modules package
from modules.account import cardpin, create_account, view_account_details, generate_account_number
import modules.transaction as tr
import modules.update as up


def main():
    print("Welcome to the Mini Bank System!")

    # Infinite loop to keep the menu running until user exits
    while True:
        print("\nPlease select an option:")
        print("1. Create Account")
        print("2. Set Card PIN")
        print("3. Update Account Details")
        print("4. View Account Details")
        print("5. Transaction")
        print("6. Exit")

        choice = input()

        # -----------------------------
        # 1. CREATE ACCOUNT
        # -----------------------------
        if choice == '1':
            account_number = generate_account_number()  # auto-generate account number
            name = input("Enter name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            balance = float(input("Enter initial balance: "))

            create_account(account_number, name, dob, address, phone, email, balance)

        # -----------------------------
        # 2. SET CARD PIN
        # -----------------------------
        elif choice == '2':
            account_number = input("Enter account number to set PIN: ")
            cardpin(account_number)

        # -----------------------------
        # 3. UPDATE ACCOUNT DETAILS
        # -----------------------------
        elif choice == '3':
            print("Update Account Details")
            account_number = input("Enter account number to update details: ")
            manager = up.AccountManager()
            manager.update_account(account_number)

        # -----------------------------
        # 4. VIEW ACCOUNT DETAILS
        # -----------------------------
        elif choice == '4':
            print("View Account Details")
            account_number = input("Enter account number to view details: ")
            view_account_details(account_number)

        # -----------------------------
        # 5. MAKE A TRANSACTION
        # -----------------------------
        elif choice == '5':
            tr.transaction_menu()

        # -----------------------------
        # 6. EXIT PROGRAM
        # -----------------------------
        elif choice == '6':
            print("Thank you for using the Mini Bank System. Goodbye!")
            break

        # -----------------------------
        # INVALID INPUT HANDLING
        # -----------------------------
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
