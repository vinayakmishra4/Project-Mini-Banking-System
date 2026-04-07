import pandas as pd

# Step 1: Load Excel file
file_name = "details.xlsx"
df = pd.read_excel(file_name)

# Step 2: Take account number input
acc_no = int(input("Enter account number: "))

# Step 3: Check if account exists
if acc_no in df["AccountNo"].values:
    
    # Get row index
    index = df[df["AccountNo"] == acc_no].index[0]
    
    print("\nAccount found!")
    print(df.loc[index])
    
    # Step 4: Ask what to update
    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Date of Birth")
    print("3. Phone")
    print("4. Address")
    print("5. Email")
    print("6. Exit")
    
    choice = input("Select an option: ")

    while True:   
        # Step 5: Update data
        if choice == "1":
            new_name = input("Enter new name: ")
            df.at[index, "Name"] = new_name
        
        elif choice == "2":
            new_dob = input("Enter new date of birth (YYYY-MM-DD): ")
            df.at[index, "Date of Birth"] = new_dob
        
        elif choice == "3":
            new_phone = input("Enter new phone: ")
            df.at[index, "Phone"] = new_phone
        
        elif choice == "4":
            new_address = input("Enter new address: ")
            df.at[index, "Address"] = new_address
        
        elif choice == "5":
            new_email = input("Enter new email: ")
            df.at[index, "Email"] = new_email
        
        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")
    
        # Step 6: Save back to Excel
        df.to_excel(file_name, index=False)
    
        print("\n✅ Details updated successfully!")
        print(df.loc[index])

else:
    print("❌ Account number not found!")