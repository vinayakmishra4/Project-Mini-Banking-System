import pandas as pd


class AccountManager:
    def __init__(self, file_name):
        # Constructor: stores the Excel file name and loads data into a DataFrame
        self.file_name = file_name
        self.df = self.load_data()

    def load_data(self):
        # Tries to load Excel file into pandas DataFrame
        # If file is missing, returns an empty DataFrame
        try:
            return pd.read_excel(self.file_name)
        except FileNotFoundError:
            print("❌ File not found!")
            return pd.DataFrame()

    def find_account(self, acc_no):
        # Searches for account number in the DataFrame
        # If found, returns the row index; otherwise returns None
        if acc_no in self.df["AccountNo"].values:
            return self.df[self.df["AccountNo"] == acc_no].index[0]
        return None

    def display_account(self, index):
        # Displays account details for a given row index
        print("\n📄 Account Details:")
        print(self.df.loc[index])

    def update_field(self, index, field, new_value):
        # Updates a specific field (column) for a given account
        self.df.at[index, field] = new_value
        
        # Save changes back to Excel file
        self.save_data()
        
        print("\n✅ Updated successfully!")
        
        # Show updated record
        self.display_account(index)

    def save_data(self):
        # Saves the current DataFrame back to the Excel file
        self.df.to_excel(self.file_name, index=False)

    def update_menu(self, index):
        # Interactive menu to update different fields of an account
        while True:
            print("\n--- UPDATE MENU ---")
            print("1. Name")
            print("2. Date of Birth")
            print("3. Phone")
            print("4. Address")
            print("5. Email")
            print("6. Exit")

            choice = input("Select an option: ")

            # Based on user choice, update specific field
            if choice == "1":
                self.update_field(index, "Name", input("Enter new name: "))

            elif choice == "2":
                self.update_field(index, "Date of Birth",
                                  input("Enter new DOB (YYYY-MM-DD): "))

            elif choice == "3":
                self.update_field(index, "Phone", input("Enter new phone: "))

            elif choice == "4":
                self.update_field(index, "Address", input("Enter new address: "))

            elif choice == "5":
                self.update_field(index, "Email", input("Enter new email: "))

            elif choice == "6":
                print("Exiting update menu...")
                break

            else:
                print("❌ Invalid choice!")

    def update_account(self, acc_no):
        # Main function to update an account
        # Step 1: Find account index
        index = self.find_account(acc_no)

        # Step 2: If account exists, show details and open update menu
        if index is not None:
            print("\n✅ Account found successfully!")
            self.display_account(index)
            self.update_menu(index)
        else:
            print("❌ Account number not found!")