# ------------------------------------------------------------
# Update Module
# Handles: finding an account and updating its stored fields.
# ------------------------------------------------------------

import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
DETAILS_FILE = os.path.join(DATA_DIR, "details.xlsx")


class AccountManager:
    def __init__(self, file_name=DETAILS_FILE):
        self.file_name = file_name
        self.df = self.load_data()

    def load_data(self):
        try:
            df = pd.read_excel(self.file_name)
            # Normalize column names (remove spaces + lowercase)
            df.columns = df.columns.str.strip().str.lower()
            return df
        except FileNotFoundError:
            print("File not found!")
            return pd.DataFrame()

    def find_account(self, acc_no):
        if self.df.empty:
            print("No data available!")
            return None

        if "account_number" not in self.df.columns:
            print("'account_number' column not found!")
            return None

        # Clean and normalize data
        self.df["account_number"] = (
            self.df["account_number"]
            .astype(str)
            .str.strip()
        )
        acc_no = str(acc_no).strip()

        result = self.df[self.df["account_number"] == acc_no]
        if not result.empty:
            return result.index[0]
        return None

    def display_account(self, index):
        print("\nAccount Details:")
        print(self.df.loc[index])

    def update_field(self, index, field, new_value):
        field = field.lower().strip()

        if field not in self.df.columns:
            print(f"Column '{field}' not found!")
            return

        # Convert column to string if updating phone/email/etc.
        if field in ["phone", "email", "account_number"]:
            self.df[field] = self.df[field].astype(str)
            new_value = str(new_value)

        self.df.at[index, field] = new_value
        self.save_data()
        print("\nUpdated successfully!")
        self.display_account(index)

    def save_data(self):
        self.df.to_excel(self.file_name, index=False)

    def update_menu(self, index):
        while True:
            print("\n--- UPDATE MENU ---")
            print("1. Name")
            print("2. Date of Birth")
            print("3. Phone")
            print("4. Address")
            print("5. Email")
            print("6. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.update_field(index, "name", input("Enter new name: "))
            elif choice == "2":
                self.update_field(index, "dob", input("Enter new DOB (YYYY-MM-DD): "))
            elif choice == "3":
                self.update_field(index, "phone", input("Enter new phone: "))
            elif choice == "4":
                self.update_field(index, "address", input("Enter new address: "))
            elif choice == "5":
                self.update_field(index, "email", input("Enter new email: "))
            elif choice == "6":
                print("Exiting update menu...")
                break
            else:
                print("Invalid choice!")

    def update_account(self, acc_no):
        index = self.find_account(acc_no)
        if index is not None:
            print("\nAccount found successfully!")
            self.display_account(index)
            self.update_menu(index)
        else:
            print("Account number not found!")
