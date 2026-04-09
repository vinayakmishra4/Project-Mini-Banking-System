# Code for the Mini Bank System
from Account import cardpin, create_account, view_account_details, generate_account_number
from Update import update_menu
from Transction import trasnctionmenu, transaction_history


class Account:
    print("Welcome to the Mini Bank System!")
    while True:
        print("\nPlease select an option:")
        print("1. Create Account")
        print("2. Set Card PIN")
        print("3. Update Account Details")
        print("4. View Account Details")
        print("5. make a transaction")
        print("6. Transaction History")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            account_number = generate_account_number()
            name = input("Enter name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            balance = float(input("Enter initial balance: "))
            create_account(account_number, name, dob, address, phone, email, balance)

        elif choice == '2':
            account_number = input("Enter account number to set PIN: ")
            cardpin(account_number)

        elif choice == '3':
            print("Update Account Details")
            account_number = input("Enter account number to update details: ")
            update_menu(account_number)

        elif choice == '4':
            print("View Account Details")
            account_number = input("Enter account number to view details: ")
            view_account_details(account_number)

        elif choice == '5':
            print("Make a transaction")
            account_number = input("Enter account number to perform transaction: ")
            trasnctionmenu(account_number, balance, transaction_history)

        elif choice == '6':
            print("Transaction History")
            account_number = input("Enter account number to view transaction history: ")
            transaction_history(account_number)

        elif choice == '7':
            print("Thank you for using the Mini Bank System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")