# ============================
# DEPOSIT FUNCTION
# ============================
def deposit(account_number, amount, balance):
    # Check if amount is valid (no negative or zero deposits)
    if amount <= 0:
        print("Invalid deposit amount")
        return balance

    # Add money to current balance
    balance += amount

    print(f"₹{amount} deposited successfully in account {account_number}")

    # Return updated balance back to main program
    return balance


# ============================
# WITHDRAW FUNCTION
# ============================
def withdraw(account_number, amount, balance):
    # Validate withdrawal amount
    if amount <= 0:
        print("Invalid withdrawal amount")
        return balance

    # Check if user has enough balance
    if balance >= amount:
        balance -= amount
        print(f"₹{amount} withdrawn successfully from account {account_number}")
    else:
        print("Insufficient balance")

    # Return updated balance
    return balance


# ============================
# TRANSFER FUNCTION
# ============================
def transfer(account_number, target_account, amount, balance):
    # Validate transfer amount
    if amount <= 0:
        print("Invalid transfer amount")
        return balance

    # Check if sender has enough money
    if balance >= amount:
        balance -= amount
        print(f"₹{amount} transferred from {account_number} to {target_account}")
    else:
        print("Insufficient balance")

    # NOTE: This is only simulation (no real receiver update)
    return balance


# ============================
# TRANSACTION HISTORY FUNCTION
# ============================
def transaction_history(account_number, history):
    print(f"\nTransaction History for account {account_number}:")

    # If no transactions exist
    if not history:
        print("No transactions yet.")
        return

    # Print each transaction stored in list
    for transaction in history:
        print(transaction)


# ============================
# MAIN MENU FUNCTION
# ============================
def transaction_menu(account_number, balance, history):

    # Loop keeps program running until user exits
    while True:
        print("\n====== TRANSACTION MENU ======")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Select an option: ")

        try:
            # ----------------------------
            # OPTION 1: DEPOSIT
            # ----------------------------
            if choice == "1":
                amount = float(input("Enter deposit amount: "))

                # Call deposit function
                balance = deposit(account_number, amount, balance)

                # Store transaction in history list
                history.append(f"Deposited ₹{amount}")

            # ----------------------------
            # OPTION 2: WITHDRAW
            # ----------------------------
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))

                # Call withdraw function
                balance = withdraw(account_number, amount, balance)

                # Store transaction in history
                history.append(f"Withdrew ₹{amount}")

            # ----------------------------
            # OPTION 3: TRANSFER
            # ----------------------------
            elif choice == "3":
                target_account = input("Enter target account number: ")
                amount = float(input("Enter transfer amount: "))

                # Call transfer function
                balance = transfer(account_number, target_account, amount, balance)

                # Store transaction in history
                history.append(f"Transferred ₹{amount} to {target_account}")

            # ----------------------------
            # OPTION 4: HISTORY
            # ----------------------------
            elif choice == "4":
                transaction_history(account_number, history)

            # ----------------------------
            # OPTION 5: EXIT
            # ----------------------------
            elif choice == "5":
                print("Exiting system... Thank you!")
                break

            else:
                print("Invalid choice! Try again.")

        # Handles wrong input like "abc"
        except ValueError:
            print("Invalid input! Please enter numeric values only.")

    # Return final updated balance
    return balance
