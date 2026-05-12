# ==============================
# Mini Bank System (Console App)
# ==============================

# Importing required functions from other modules

from Account import cardpin, create_account, view_account_details, generate_account_number
import transction as tr
import Update as up

class Account:
    # Program starts here (runs immediately when file is executed)
    
    print("Welcome to the Mini Bank System!")

    # Infinite loop to keep the menu running until user exits
    while True:

        # Displaying main menu options
        print("\nPlease select an option:")
        print("1. Create Account")
        print("2. Set Card PIN")
        print("3. Update Account Details")
        print("4. View Account Details")
        print("5. Transaction")
        print("6. Exit")

        # Taking user input for menu selection
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

            # Create and store account details
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
            manager=up.AccountManager('details.xlsx')  # Create an instance of AccountManager to access update functions
            manager.update_account(account_number)  # Call the update_account method with the provided account number

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
            tr.transaction_menu()  # Call the transaction menu function from the transction module

        # ----------------------------
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