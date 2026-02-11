# 📘 Dictionaries, Sets & Python Standard Library — Complete Guide

---

## 🧩 Dictionaries

### 🔹 What is a Dictionary?

A **dictionary** is a built-in Python data structure that stores data in **key–value pairs**.

Think of it like:

* A **real dictionary** → word (key) : meaning (value)
* A **phone contact** → name (key) : phone number (value)

---

### 🔹 Key Characteristics

* Keys must be **immutable**

  * ✅ Allowed: `str`, `int`, `float`, `tuple`
  * ❌ Not allowed: `list`, `set`, `dict`
* Values can be **any data type**
* Dictionaries are **mutable**
* From Python 3.7+, dictionaries **preserve insertion order**

---

### 🔹 General Syntax

```python
dictionary = {
    key1: value1,
    key2: value2
}
```

---

### 🔹 Example

```python
student = {
    "name": "Rahul",
    "age": 22,
    "marks": 85
}
```

---

## 🏗️ Creating Dictionaries

### 1️⃣ Using Curly Braces

```python
pizza = {
    "name": "Margherita",
    "price": 8.9,
    "calories": 250
}
```

---

### 2️⃣ Using `dict()` Constructor

Useful when data already exists as **key–value pairs**.

```python
pizza = dict([
    ('name', 'Margherita Pizza'),
    ('price', 8.9),
    ('calories_per_slice', 250),
    ('toppings', ['mozzarella', 'basil'])
])
```

📌 **Rule:** Each tuple must have **exactly 2 elements**.

---

## 🔑 Accessing Dictionary Values

### Bracket Notation

```python
pizza["price"]
```

⚠️ **Problem:** Raises `KeyError` if key doesn’t exist.

---

### `get()` Method (Safe Way)

```python
pizza.get("price", 0)
```

✔ Returns default value if key is missing
✔ Avoids runtime errors

---

## 🔧 Common Dictionary Methods

### `keys()`

Returns all keys as a **view object**.

```python
pizza.keys()
```

---

### `values()`

Returns all values.

```python
pizza.values()
```

---

### `items()`

Returns key–value pairs as tuples.

```python
pizza.items()
```

---

### `clear()`

Deletes everything from the dictionary.

```python
pizza.clear()
```

📌 Dictionary still exists but is empty.

---

### `pop(key, default)`

Removes a key and returns its value.

```python
pizza.pop("price", 0)
```

⚠️ Without default → `KeyError` if key not found.

---

### `popitem()`

Removes **last inserted item** (Python 3.7+).

```python
pizza.popitem()
```

---

### `update()`

Adds or updates multiple key–value pairs.

```python
pizza.update({
    "price": 15,
    "delivery_time": 30
})
```

✔ Overwrites existing keys
✔ Adds new keys if not present

---

## 🔁 Looping Through Dictionaries

### Loop Over Values

```python
for price in products.values():
    print(price)
```

---

### Loop Over Keys

```python
for product in products:
    print(product)
```

---

### Loop Over Key–Value Pairs

```python
for product, price in products.items():
    print(product, price)
```

📌 Best approach when **both key & value** are needed.

---

### `enumerate()` with Dictionaries

Adds an index counter.

```python
for index, item in enumerate(products.items(), 1):
    print(index, item)
```

✔ Useful for numbered lists or menus.

---

## 🔢 Sets

### 🔹 What is a Set?

A **set** is a collection of **unique, unordered elements**.

Think of it like:

* A **bag of unique items**
* No duplicates allowed

---

### 🔹 Key Characteristics

* No duplicate values
* Unordered (no index access)
* Mutable
* Only immutable elements allowed

---

### Defining a Set

```python
my_set = {1, 2, 3, 4, 5}
```

---

### Empty Set (Important!)

```python
set()   # Correct
{}      # Dictionary
```

---

## 🔧 Common Set Methods

### `add()`

```python
my_set.add(6)
```

---

### `remove()` vs `discard()`

```python
my_set.remove(4)   # Error if missing
my_set.discard(4)  # No error
```

📌 Prefer `discard()` when unsure.

---

### `clear()`

```python
my_set.clear()
```

---

## 🧮 Mathematical Set Operations

### Subset

```python
small_set.issubset(big_set)
```

---

### Superset

```python
big_set.issuperset(small_set)
```

---

### Disjoint Sets

```python
set1.isdisjoint(set2)
```

✔ True → no common elements

---

### Union `|`

```python
set1 | set2
```

✔ Combines all unique elements

---

### Intersection `&`

```python
set1 & set2
```

✔ Only common elements

---

### Difference `-`

```python
set1 - set2
```

✔ Elements in first set only

---

### Symmetric Difference `^`

```python
set1 ^ set2
```

✔ Elements in either set, not both

---

### Membership Test

```python
5 in my_set
```

✔ Very fast operation

---

## 📦 Python Standard Library

### What is a Library?

A **library** is reusable, pre-written code.

Python’s **standard library** comes built-in—no installation needed.

---

### Popular Modules

* `math` → mathematical functions
* `random` → randomness
* `re` → regular expressions
* `datetime` → date & time handling

---

## 📥 Import Statements

### Basic Import

```python
import math
math.sqrt(36)
```

---

### Import with Alias

```python
import math as m
m.sqrt(36)
```

✔ Cleaner
✔ Avoids name conflicts

---

### Import Specific Elements

```python
from math import sin, cos
```

✔ Shorter code
⚠ Risk of naming conflicts

---

### Import with Aliases

```python
from math import sin as s
```

---

### Import Everything (❌ Avoid)

```python
from math import *
```

❌ Hard to debug
❌ Pollutes namespace

---

## 🚦 `if __name__ == "__main__"`

### What is `__name__`?

* `"__main__"` → script run directly
* module name → imported elsewhere

---

### Why Use It?

* Prevents unwanted execution during import
* Separates **logic** from **execution**

---

### Example

```python
if __name__ == "__main__":
    main()
```

✔ Best practice
✔ Professional code structure

---

## ✅ Final Summary

### Dictionaries

* Store structured data
* Fast lookup
* Key–value mapping

### Sets

* Remove duplicates
* Perform mathematical operations
* Fast membership testing

### Standard Library

* Saves time
* Avoids reinventing the wheel
* Essential for real-world Python

---