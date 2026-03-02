from datetime import datetime

class Transaction:
    def __init__(self, type, amount, timestamp=None, note=None):
        self.type = type
        self.amount = amount
        self.timestamp = timestamp if timestamp else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.note = note
    def __str__(self):
        return f"[{self.timestamp}] Account Type: {self.type} | Amount: {self.amount}"

class BankAccount:
    def __str__(self, balance=0, transactions=[]):
        self.balance = balance
        self.transactions = transactions

class Customer:
    def __str__(self, name, account):
        self.name = name
        self.account = account


def main():
    tipu = Customer('Tipu')


if __file__ == '__main__':
    main()
