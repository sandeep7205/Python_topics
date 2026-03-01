**minimal structured starter skeleton** for the Bank Account Simulator.

---

# 🏦 BANK ACCOUNT SIMULATOR — STARTER SKELETON

Copy this and start implementing step by step.

```python
"""
============================================================
BANK ACCOUNT SIMULATOR
============================================================

PROJECT GOAL:
Understand object references and class relationships.

LINKING TREE:

Customer
   └── has → BankAccount
                └── has → list of Transaction objects

IMPORTANT CONCEPT:
BankAccount stores Transaction OBJECTS (not strings).
Customer delegates actions to BankAccount.
============================================================
"""

import datetime


# ============================================================
# TRANSACTION CLASS
# ============================================================
class Transaction:
    """
    Responsibility:
    - Represent a single deposit or withdrawal
    - Store type, amount, timestamp
    - Provide readable string representation
    """

    def __init__(self, transaction_type, amount):
        # TODO:
        # Store transaction type (deposit / withdrawal)
        # Store amount
        # Store timestamp (use datetime.datetime.now())
        pass

    def __str__(self):
        """
        Should return something like:
        '2026-03-02 10:30 | Deposit | 500'
        """
        # TODO: Return formatted string
        pass


# ============================================================
# BANK ACCOUNT CLASS
# ============================================================
class BankAccount:
    """
    Responsibility:
    - Store balance
    - Store list of Transaction objects
    - Handle deposit and withdrawal logic
    """

    def __init__(self):
        # TODO:
        # Initialize balance to 0
        # Initialize empty list for transactions
        pass

    def deposit(self, amount):
        """
        Steps:
        1. Validate amount > 0
        2. Increase balance
        3. Create Transaction object
        4. Append Transaction object to transactions list
        """
        pass

    def withdraw(self, amount):
        """
        Steps:
        1. Validate amount > 0
        2. Check if balance is sufficient
        3. Deduct from balance
        4. Create Transaction object
        5. Append to transactions list
        """
        pass

    def show_balance(self):
        """
        Print or return current balance
        """
        pass

    def show_transactions(self):
        """
        Loop through transaction list
        Print each transaction
        """
        pass


# ============================================================
# CUSTOMER CLASS
# ============================================================
class Customer:
    """
    Responsibility:
    - Represent a bank customer
    - Own a BankAccount object
    - Delegate actions to BankAccount
    """

    def __init__(self, name):
        # TODO:
        # Store name
        # Create BankAccount object and assign to self.account
        pass

    def deposit(self, amount):
        # TODO:
        # Call self.account.deposit(amount)
        pass

    def withdraw(self, amount):
        # TODO:
        # Call self.account.withdraw(amount)
        pass

    def check_balance(self):
        # TODO:
        # Call self.account.show_balance()
        pass

    def view_transactions(self):
        # TODO:
        # Call self.account.show_transactions()
        pass


# ============================================================
# MAIN FUNCTION (TEST FLOW)
# ============================================================
def main():
    """
    Suggested Testing Steps:

    1. Create Customer
    2. Deposit money
    3. Withdraw money
    4. Check balance
    5. View transaction history
    """

    # TODO:
    # Create customer object
    # Call deposit()
    # Call withdraw()
    # Call check_balance()
    # Call view_transactions()
    pass


if __name__ == "__main__":
    main()
```

---

# 🚀 How You Should Build This (Follow Strictly)

### Step 1:

Implement only `Transaction.__init__`

Run:

```python
t = Transaction("deposit", 500)
print(t)
```

Fix until it prints correctly.

---

### Step 2:

Implement `BankAccount.__init__`

Test:

```python
acc = BankAccount()
print(acc.balance)
print(acc.transactions)
```

---

### Step 3:

Implement `deposit()`

Test:

```python
acc.deposit(500)
print(acc.balance)
print(acc.transactions[0])
```

---

### Step 4:

Implement `withdraw()`

Test both:

* Valid withdrawal
* Invalid (insufficient balance)

---

### Step 5:

Implement Customer delegation methods

Test full flow in `main()`.

---

# 🎯 Important Mental Reminder

When you do:

```python
self.transactions.append(transaction)
```

You are storing a FULL Transaction object.

Later when you do:

```python
self.transactions[0]
```

You are getting that same object back.

Same concept as Email simulator.

---

## BASIC FUNCTIONAL TEST (Step-by-step flow)
```python
def main():
    print("=== BANK SIMULATOR TEST START ===\n")

    # 1️⃣ Create Customer
    rahul = Customer("Rahul")

    # 2️⃣ Check initial balance
    print("Checking initial balance:")
    rahul.check_balance()   # Expect: 0

    # 3️⃣ Deposit money
    print("\nDepositing 1000:")
    rahul.deposit(1000)     # Expect balance = 1000

    # 4️⃣ Withdraw valid amount
    print("\nWithdrawing 300:")
    rahul.withdraw(300)     # Expect balance = 700

    # 5️⃣ Withdraw more than balance (should fail)
    print("\nTrying to withdraw 1000 (should fail):")
    rahul.withdraw(1000)    # Expect error / no balance change

    # 6️⃣ Check final balance
    print("\nChecking final balance:")
    rahul.check_balance()   # Expect: 700

    # 7️⃣ View transaction history
    print("\nViewing transactions:")
    rahul.view_transactions()  # Expect: 2 transactions only

    print("\n=== BANK SIMULATOR TEST END ===")

```