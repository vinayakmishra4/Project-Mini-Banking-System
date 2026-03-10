# Transaction class for handling banking transactions
file='details.json'


class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def execute(self):
        if self.transaction_type == "deposit":
            self.account.balance += self.amount
        elif self.transaction_type == "withdrawal":
            if self.account.balance >= self.amount:
                self.account.balance -= self.amount
            else:
                print("Insufficient funds")
        else:
            print("Invalid transaction type")