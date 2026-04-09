import pandas as pd


def __init__(self, file_name):
        self.file_name = file_name
        self.df = self.load_data()

def load_data(self):
        try:
            return pd.read_excel(self.file_name)
        except FileNotFoundError:
            print("❌ File not found!")
            return pd.DataFrame()

def find_account(self, acc_no):
        if acc_no in self.df["AccountNo"].values:
            return self.df[self.df["AccountNo"] == acc_no].index[0]
        return None

def display_account(self, index):
        print("\n📄 Account Details:")
        print(self.df.loc[index])

def update_field(self, index, field, new_value):
        self.df.at[index, field] = new_value
        self.save_data()
        print("\n✅ Updated successfully!")
        self.display_account(index)

def save_data(self):
        self.df.to_excel(self.file_name, index=False)

def update_menu(self, index):
        while True:
            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Date of Birth")
            print("3. Phone")
            print("4. Address")
            print("5. Email")
            print("6. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.update_field(index, "Name", input("Enter new name: "))

            elif choice == "2":
                self.update_field(index, "Date of Birth", input("Enter new DOB (YYYY-MM-DD): "))

            elif choice == "3":
                self.update_field(index, "Phone", input("Enter new phone: "))

            elif choice == "4":
                self.update_field(index, "Address", input("Enter new address: "))

            elif choice == "5":
                self.update_field(index, "Email", input("Enter new email: "))

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("❌ Invalid choice!")

def update_account(self, acc_no):
        index = self.find_account(acc_no)

        if index is not None:
            print("\n✅ Account found!")
            self.display_account(index)
            self.update_menu(index)
        else:
            print("❌ Account number not found!")