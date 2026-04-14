import pandas as pd


class AccountManager:
    def __init__(self, file_name):
        # Constructor:
        # Stores Excel file name and loads data into a DataFrame when object is created
        self.file_name = file_name
        self.df = self.load_data()

    def load_data(self):
        # Loads Excel file into pandas DataFrame
        # If file does not exist, returns an empty DataFrame instead of crashing
        try:
            return pd.read_excel(self.file_name)
        except FileNotFoundError:
            print("❌ File not found!")
            return pd.DataFrame()

    def find_account(self, acc_no):
        # Searches for account number in the DataFrame
        # Returns the index of the matching row if found, otherwise returns None

        # Check if account number exists in the column values
        if acc_no in self.df["AccountNo"].values:
            # Filter rows where AccountNo matches and return first index
            return self.df[self.df["AccountNo"] == acc_no].index[0]

        # If not found
        return None

    def display_account(self, index):
        # Displays full details of the account using row index
        print("\n📄 Account Details:")

        # loc[] is used to access row by index label
        print(self.df.loc[index])

    def update_field(self, index, field, new_value):
        # Updates a specific column (field) for a given account row

        # .at is used for fast single-cell update
        self.df.at[index, field] = new_value

        # Save updated DataFrame back to Excel file immediately
        self.save_data()

        print("\n✅ Updated successfully!")

        # Show updated record to user for confirmation
        self.display_account(index)

    def save_data(self):
        # Saves current DataFrame into Excel file
        # index=False prevents pandas from writing row index into Excel
        self.df.to_excel(self.file_name, index=False)

    def update_menu(self, index):
        # Interactive menu that allows user to update different fields

        while True:
            print("\n--- UPDATE MENU ---")
            print("1. Name")
            print("2. Date of Birth")
            print("3. Phone")
            print("4. Address")
            print("5. Email")
            print("6. Exit")

            # Take user input for choice
            choice = input("Select an option: ")

            # Based on choice, update specific column in DataFrame
            if choice == "1":
                self.update_field(index, "Name", input("Enter new name: "))

            elif choice == "2":
                self.update_field(
                    index,
                    "Date of Birth",
                    input("Enter new DOB (YYYY-MM-DD): ")
                )

            elif choice == "3":
                self.update_field(index, "Phone", input("Enter new phone: "))

            elif choice == "4":
                self.update_field(index, "Address", input("Enter new address: "))

            elif choice == "5":
                self.update_field(index, "Email", input("Enter new email: "))

            elif choice == "6":
                # Exit loop and return to previous function
                print("Exiting update menu...")
                break

            else:
                # Handles invalid menu input
                print("❌ Invalid choice!")

    def update_account(self, acc_no):
        # Main function to update an account

        # Step 1: Find account index using account number
        index = self.find_account(acc_no)

        # Step 2: If account exists, show details and open update menu
        if index is not None:
            print("\n✅ Account found successfully!")

            # Show current account data before update
            self.display_account(index)

            # Open interactive update menu
            self.update_menu(index)
        else:
            # If account number not found in DataFrame
            print("❌ Account number not found!")