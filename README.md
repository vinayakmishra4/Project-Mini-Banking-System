# 🏦 Mini Banking System

A console-based **Mini Banking System** built in Python that simulates core banking operations — creating accounts, setting card PINs, updating account details, viewing account information, and performing transactions (deposit/withdraw) with a persistent transaction history. All data is stored locally using Excel files, no external database required.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/storage-Excel%20(.xlsx)-217346?logo=microsoft-excel&logoColor=white)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🆕 **Create Account** | Generates a unique 10-digit account number and stores customer details (name, DOB, address, phone, email, balance) |
| 🔐 **Set Card PIN** | Set or update a validated 4-digit PIN for any account |
| ✏️ **Update Account Details** | Modify name, date of birth, phone, address, or email for an existing account |
| 👀 **View Account Details** | Look up and display full account information by account number |
| 💰 **Deposit / Withdraw** | Update account balance, with insufficient-balance protection on withdrawals |
| 📜 **Transaction History** | View a full log of every deposit and withdrawal per account |
| 💾 **Persistent Storage** | All data is saved to Excel files, so nothing is lost between runs |

---

## 🗂️ Project Structure

```
Project-Mini-Banking-System/
├── mbs.py                # entry point — run this
├── modules/
│   ├── __init__.py
│   ├── account.py          (was Account.py)
│   ├── transaction.py      (was transction.py — typo fixed)
│   └── update.py           (was Update.py)
├── data/
│   ├── details.xlsx        (created on first run)
│   └── pin.xlsx             (created on first run)
├── requirements.txt
├── .gitignore
└── README.md
```

<details>
<summary>📌 View source files on GitHub</summary>

<br>

**🚀 `mbs.py`**
Main entry point — displays the menu and routes user choices
`https://github.com/vinayakmishra4/Project-Mini-Banking-System/blob/main/mbs.py`

**🧾 `modules/account.py`**
Account creation, account number generation, PIN setup, view details
`https://github.com/vinayakmishra4/Project-Mini-Banking-System/blob/main/modules/account.py`

**💸 `modules/transaction.py`**
Deposit, withdraw, balance updates, transaction history
`https://github.com/vinayakmishra4/Project-Mini-Banking-System/blob/main/modules/transaction.py`

**✏️ `modules/update.py`**
`AccountManager` class — find and update account fields
`https://github.com/vinayakmishra4/Project-Mini-Banking-System/blob/main/modules/update.py`

**📦 `requirements.txt`**
Project dependencies
`https://github.com/vinayakmishra4/Project-Mini-Banking-System/blob/main/requirements.txt`

</details>

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** [pandas](https://pandas.pydata.org/), [openpyxl](https://openpyxl.readthedocs.io/)
- **Storage:** Excel (`.xlsx`) files — no external database needed

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vinayakmishra4/Project-Mini-Banking-System.git
   cd Project-Mini-Banking-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python mbs.py
   ```

---

## 📖 Usage

When you run `mbs.py`, you'll see the main menu:

```
Please select an option:
1. Create Account
2. Set Card PIN
3. Update Account Details
4. View Account Details
5. Transaction
6. Exit
```

- Choosing **Transaction** (option 5) opens a submenu for Deposit, Withdraw, View Transaction History, or Exit.
- Choosing **Update Account Details** (option 3) lets you find an account and edit Name, DOB, Phone, Address, or Email.
- All account data is auto-saved to `data/details.xlsx`, and PINs are saved separately to `data/pin.xlsx`.

---

## 🧾 How Data Is Stored

- **`details.xlsx`** — main sheet holds account number, name, DOB, address, phone, email, and balance. A second sheet, `TransactionHistory`, logs every deposit/withdrawal with account number, type, amount, and timestamp.
- **`pin.xlsx`** — maps account numbers to their 4-digit PINs.

---

## ⚠️ Known Issues / Limitations

- No login/authentication flow — PIN is stored but not currently used to gate access to account actions.
- No input sanitization beyond basic PIN validation; invalid data (e.g. malformed email/phone) can still be saved.
- Uses Excel files as a "database," which doesn't scale well and isn't safe for concurrent access.
- No unit tests currently included.
- Account deletion is not supported.

---

## 🔮 Future Improvements

- Add PIN-based authentication before allowing transactions or viewing details.
- Migrate from Excel storage to a proper database (e.g. SQLite) for reliability and concurrency.
- Add input validation for email, phone number, and date formats.
- Add the ability to delete/close an account.
- Add unit tests for core modules (`account.py`, `transaction.py`, `update.py`).
- Add a simple GUI (e.g. Tkinter) as an alternative to the console interface.

---

⭐ If you found this project useful, consider giving it a star on [GitHub](https://github.com/vinayakmishra4/Project-Mini-Banking-System)!