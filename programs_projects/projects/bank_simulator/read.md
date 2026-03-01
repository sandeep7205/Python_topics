# Project: Bank Account Simulator — Full Roadmap & Checklist

---

## Project Goal (one sentence)

Build a small console bank simulator to practice composition and object references: `Customer` has a `BankAccount`, `BankAccount` stores a list of `Transaction` objects; customers deposit, withdraw, view balance and transaction history.

---

# OVERVIEW: deliverables you'll produce

* A single Python file (or small package) containing `Customer`, `BankAccount`, `Transaction`, and a small interactive or scripted `main()` that demonstrates the flow.
* README comment at top describing relationships (linking tree + memory notes).
* Unit-style manual tests (assert-like checks in a separate test function or simple printed checks).
* Inline docstrings + comments explaining object ownership and method responsibilities.
* Several small feature extensions (transfer, persist, interest) as optional extras.

---

# DESIGN & MENTAL MODEL (read before you code)

* Entities:

  * `Customer` — owns a `BankAccount`
  * `BankAccount` — stores `balance` and `transactions` (list of `Transaction` objects)
  * `Transaction` — stores `type` ('deposit'/'withdrawal'/'transfer'), `amount`, `timestamp`, maybe `note`
* Flow examples:

  * `customer.deposit(amount)` → delegates to `account.deposit(amount)` → `account` creates `Transaction` and appends to `transactions`, updates `balance`.
  * `customer.view_transactions()` → delegates to `account.show_transactions()` → prints each `Transaction` (calls `__str__`).
* Key principle: objects store objects (account stores transaction objects); methods should operate on owned data.

---

# PHASE 0 — PREP (very short)

* Create a new folder / Git repo (optional).
* Create main file `bank_simulator.py`.
* Add top comment block with:

  * Short project description
  * Linking tree (like you asked earlier)
  * Memory reference diagram note

Checklist:

* [ ] repo/folder created
* [ ] `bank_simulator.py` created
* [ ] top comment linking tree pasted

---

# PHASE 1 — SCAFFOLD (skeleton classes & docs)

Tasks (implement only class skeletons and docstrings):

1. Create class `Transaction` with `__init__(self, type, amount, timestamp=None, note=None)` and `__str__` docstring.
2. Create class `BankAccount` with attributes: `balance` (start 0 or given), `transactions` (empty list). Add docstring describing responsibilities.
3. Create class `Customer` with attributes: `name`, `account` (BankAccount). Add docstring.
4. Create `main()` stub that creates one `Customer` object and prints a message.

What to write in docstrings/comments:

* Which class owns what data.
* Which methods should **not** be in that class (e.g., `Customer` should not directly manipulate `transactions` list).
* Example object relationships (one-line).

Checklist:

* [ ] `Transaction` class skeleton
* [ ] `BankAccount` class skeleton
* [ ] `Customer` class skeleton
* [ ] `main()` stub with simple instantiation

---

# PHASE 2 — CORE BEHAVIOR (build minimal working functionality)

Implement methods step-by-step. After each method, run the small manual test.

### Step 2.1: Transaction

* Implement `__init__` to store `type` and `amount` and `timestamp` (use `datetime.now()` if None).
* Implement `__str__` that returns e.g. `"YYYY-MM-DD HH:MM - deposit - 500"`.
  Manual test:
* Create `Transaction('deposit', 500)` in `main()` and `print(transaction)`.

Checklist:

* [ ] Transaction init + `__str__` working

### Step 2.2: BankAccount: deposit()

* Method signature: `deposit(self, amount, note=None)`
* Behavior:

  * Validate amount > 0 (if invalid, raise ValueError or print error)
  * Increase `self.balance` by `amount`
  * Create Transaction object `Transaction('deposit', amount, note=note)` and append to `self.transactions`
  * Return the new balance or the new Transaction object
    Manual test:
* In `main()`, call `acc.deposit(500)`, then `print(acc.balance)` and `print(acc.transactions[0])`.

Checklist:

* [ ] deposit() updates balance and appends Transaction

### Step 2.3: BankAccount: withdraw()

* Method signature: `withdraw(self, amount, note=None)`
* Behavior:

  * Validate amount > 0
  * Check `self.balance >= amount` ; if not, print error / return False
  * Deduct from balance
  * Create Transaction('withdrawal', amount) and append
  * Return new balance or True
    Manual tests:
* Withdraw less than balance → success
* Withdraw more than balance → failure (balance unchanged, no transaction)

Checklist:

* [ ] withdraw() implemented and tested (both success and insufficient funds)

### Step 2.4: BankAccount: show_transactions()

* Should loop through `self.transactions` and print numbered list calling `str(transaction)`
  Manual test:
* After few deposits/withdrawals, call `acc.show_transactions()` and check output formatting.

Checklist:

* [ ] transaction history printed correctly

### Step 2.5: Customer methods (thin wrappers)

* `Customer.deposit(amount)`: call `self.account.deposit(amount)` and print confirmation.
* `Customer.withdraw(amount)`: call `self.account.withdraw(amount)`
* `Customer.check_balance()`: print `self.account.balance`
* `Customer.view_transactions()`: call `self.account.show_transactions()`

Manual test:

* In `main()`, create a customer, call deposit, withdraw, check balance, view transactions, check outputs.

Checklist:

* [ ] Customer wrappers working

---

# PHASE 3 — MANUAL TEST SUITE (simple asserts you can run)

Add a `test()` function in the file that runs a set of checks (use `assert` or printed expected vs actual):

Example checks to include:

* After deposit of X, balance increased by X.
* After withdraw of Y (where Y <= balance), balance decreased by Y.
* After failed withdraw (insufficient funds), balance unchanged.
* Transaction list length equals number of successful operations.
* Transaction objects have correct types and amounts.

Checklist:

* [ ] `test()` function added
* [ ] All asserts pass manually

---

# PHASE 4 — CLI / Scripted Demo (make it interactive)

Add a simple loop in `main()` or a `demo()` function to demonstrate usage:

Options to provide:

* `d` deposit
* `w` withdraw
* `b` balance
* `t` transactions
* `q` quit

Important design points:

* Keep UI and business logic separated (CLI should only call methods).
* Always validate user input strings to floats carefully.

Manual test:

* Run the demo and try deposit/withdraw sequences. Observe `Transaction` objects printed.

Checklist:

* [ ] CLI demo implemented
* [ ] UI calls only delegate to object methods

---

# PHASE 5 — REFINE & DOCUMENT

* Add docstrings to every method explaining parameters, returns, and exceptions.
* Add inline comments where object references are created or used (e.g., `# appending Transaction OBJECT, not string`).
* Add top-of-file linking tree and memory reference block (paste the one you liked).
* Add minimal README lines inside file header explaining how to run the demo.

Checklist:

* [ ] Docstrings for each class/method
* [ ] Top-of-file linking tree + memory notes present

---

# PHASE 6 — EXTENSIONS (pick any; do one at a time)

Each extension reinforces the same OOP concept.

Extensions (ordered by learning value):

1. **Transfer**: implement `account.transfer_to(other_account, amount)` which creates two transactions (withdrawal on source, deposit on target) and updates both balances. Test references (transaction stores parties?).

   * Key learning: objects referencing other objects (transfer points to other account object).

2. **Transaction types with metadata**: add `note`, `counterparty` on transactions and print them.

3. **Multiple Customers & Bank class**: Add `Bank` that stores customers and can look them up by name. `Bank` handles transfers between customers.

4. **Save/Load**: persist accounts/transactions to JSON (practice serializing objects — convert to dictionaries). This teaches object → primitive conversions.

5. **Interest calculation**: add `apply_interest(rate)` method on `BankAccount`.

6. **Unit tests**: create simple `tests.py` with `unittest` or simple functions.

Pick one extension, implement, test, then pick the next.

Checklist per extension:

* [ ] extension implemented
* [ ] tests exist and pass

---

# CHECKPOINTS & WHAT TO LOOK FOR (debugging checklist)

Whenever something fails, go through this checklist:

1. **Is the object being passed or a copy?**

   * Print `type(obj)` or `print(obj)` to see whether you have an object reference.
2. **Are you appending objects to the list?**

   * Print `self.transactions` and `type(self.transactions[0])`.
3. **Is `balance` updated as expected?**

   * Print balance before and after method call.
4. **Off-by-one errors in indexing?**

   * If using user-facing 1-based indexes, convert to 0-based internally.
5. **Method signature mismatch** (e.g., missing `self` in instance method).
6. **Wrong variable used** (e.g., using `amount` vs `self.amount`).
7. **Accidental shadowing**: local variable named same as attribute.
8. **Return values ignored**: if method returns new balance, ensure caller uses it or prints it.
9. **Transaction creation on failed operations**: ensure you do NOT create a transaction when an operation fails.
10. **Prints vs Returns**: decide whether methods should `return` values (preferred for logic) or `print` (for demo).

---

# SAMPLE MANUAL TEST CASES (copy to `main()` or `test()` to run)

(Use these to verify behavior by eye or assert)

1. Create customer `C` and account `A`.
2. `C.deposit(1000)` → expect `A.balance == 1000` and transactions length 1, transaction type 'deposit', amount 1000.
3. `C.withdraw(200)` → expect `A.balance == 800` and transactions length 2.
4. `C.withdraw(1000)` → insufficient funds: `A.balance` still 800 and transactions length still 2.
5. `C.view_transactions()` prints 2 transactions in order (oldest → newest).

Make these checks using `assert` if you want automatic failure.

---

# GOOD PRACTICES & STYLE NOTES (tiny details)

* Use `self` as the first parameter in every instance method.
* Keep responsibilities small: account handles balance/transactions, customer only interfaces.
* Use `datetime.datetime.now()` in Transaction if timestamp not provided.
* Use `__str__` on `Transaction` so printing works cleanly.
* Prefer returning status or the created `Transaction` from `deposit()` and `withdraw()` (instead of printing) — easier to test.
* For amounts, choose `float` or `Decimal` (Decimal is financially accurate, but float is OK for practice).
* Write clear commit messages:

  * `init: add class skeletons`
  * `feat: implement deposit/withdraw`
  * `test: add basic test cases`
  * `refactor: add CLI and docstrings`

---

# SMALL DAILY PRACTICE SUGGESTIONS (how to practice without fatigue)

* Work in short focused chunks. After you finish each checklist step, run tests and confirm behavior.
* After each completed method, add a one-line comment explaining why that method belongs to that class.

---

# COMMON PITFALLS (and how to avoid them)

* Creating Transaction before checking funds (so failed withdrawal still creates transaction) → fix by validating first, then creating Transaction only on success.
* Forgetting to add `self` to method signatures → causes TypeError.
* Appending strings instead of objects to transaction list → test `type(self.transactions[0])`.
* Printing in core logic (makes testing harder) → prefer returning values from logic methods; print only in CLI/demo layer.

---

# EXERCISE QUESTIONS (self-check after each phase)

Answer these in comments or a notebook after Phase 2:

1. When `cust.deposit(100)` runs, which object creates the `Transaction`? Which object stores it?
2. If you print `acc.transactions[0]`, what will be printed and why?
3. What changes if `Customer` stores transactions directly instead of BankAccount?
4. If you pass `other_customer.account` into `account.transfer_to()`, explain how references change.

If you can answer these confidently, you’ve internalized references.

---

# OPTIONAL: HOW TO STRUCTURE YOUR GIT BRANCHES (if using git)

* `main` — keep stable demo
* `feature/skeleton` — initial classes
* `feature/core` — deposit/withdraw
* `feature/cli` — CLI
* `feature/transfer` — transfer extension

Commit after each checklist item with the short commit messages suggested above.

---

# FINAL MOTIVATIONAL NOTE

This project mirrors the Email Simulator structure exactly (a `User` owns a container object which stores object instances). Building it yourself and following the checklist will make the memory/reference relationship click. If you get stuck at any checklist item, paste the minimal failing code / failing prints and I’ll walk you through the exact line-by-line reason and fix.

---

