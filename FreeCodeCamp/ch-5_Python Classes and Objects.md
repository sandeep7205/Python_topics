# Python Classes and Objects – Detailed Review

## 1. What is a Class?

A **class** is like a **blueprint or template** used to create objects.

Think about a **real-world example**:

* A **Car blueprint** defines what a car should have:

  * color
  * model
  * engine
  * speed
* But the blueprint itself is **not a real car**.

Using that blueprint, manufacturers create **actual cars**.

Similarly in Python:

* **Class → blueprint**
* **Object → real instance created from the blueprint**

---

## Basic Class Definition

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name.upper()} says woof woof!')
```

### Explanation

`class Dog:`

Defines a new class called **Dog**.

`__init__`

* This is a **constructor method**.
* It runs **automatically when an object is created**.
* Used to initialize object attributes.

`self`

* Refers to **the current object instance**.
* Every method inside a class must receive `self` as the first parameter.

Attributes created:

```
self.name
self.age
```

These belong to **each individual object**.

---

# 2. Creating Objects (Instances)

Objects are **instances of a class**.

Example:

```python
dog1 = Dog('Jack', 3)
dog2 = Dog('Thatcher', 5)
```

Here:

| Object | name     | age |
| ------ | -------- | --- |
| dog1   | Jack     | 3   |
| dog2   | Thatcher | 5   |

Each object has **its own data**.

---

# 3. Calling Methods on Objects

Methods are **functions inside a class**.

Example:

```python
dog1.bark()
dog2.bark()
```

Output:

```
JACK says woof woof!
THATCHER says woof woof!
```

How it works internally:

```
dog1.bark()
```

Python internally calls:

```
Dog.bark(dog1)
```

So `self` becomes `dog1`.

---

# 4. Difference Between Class and Object

| Class              | Object               |
| ------------------ | -------------------- |
| Blueprint          | Actual instance      |
| Defines properties | Contains real values |
| Created once       | Can create many      |

Example:

```
class Dog  → blueprint
dog1       → object
dog2       → object
dog3       → object
```

---

# 5. Attributes in Classes

Attributes store **data about an object**.

There are **two types of attributes**.

---

# 5.1 Instance Attributes

These belong to **each individual object**.

Defined inside `__init__`.

Example:

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

Example usage:

```python
dog1 = Dog("Jack")
dog2 = Dog("Rocky")

print(dog1.name)
print(dog2.name)
```

Output:

```
Jack
Rocky
```

Each object stores **its own value**.

---

# 5.2 Class Attributes

These belong to the **class itself** and are shared by all objects.

Example:

```python
class Dog:
    species = "French Bulldog"

    def __init__(self, name):
        self.name = name
```

Usage:

```python
print(Dog.species)

jack = Dog("Jack")

print(jack.name)
print(jack.species)
```

Output:

```
French Bulldog
Jack
French Bulldog
```

Both objects share the **same species value**.

---

# 6. Methods in Classes

A **method** is a function defined inside a class.

Methods usually:

* read object data
* modify object data
* perform actions

Example:

```python
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def describe(self):
        return f"This car is a {self.color} {self.model}"
```

Creating objects:

```python
my_car_1 = Car("red", "Tesla Model S")
```

Calling method:

```python
print(my_car_1.describe())
```

Output:

```
This car is a red Tesla Model S
```

---

# 7. Dot Notation

Methods and attributes are accessed using **dot notation**.

```
object.attribute
object.method()
```

Example:

```python
my_car_1.color
my_car_1.describe()
```

---

# 8. Dunder (Magic) Methods

Dunder methods are **special methods** that Python automatically calls.

They start and end with:

```
__methodname__
```

Examples:

```
__init__
__str__
__len__
__eq__
__add__
__iter__
```

These allow Python objects to behave like **built-in objects**.

---

# Example: Book Class with Dunder Methods

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"{self.title} has {self.pages} pages"

    def __eq__(self, other):
        return self.pages == other.pages
```

Creating objects:

```python
book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Money Mastery", 420)
```

Using built-in operations:

```python
print(len(book1))
print(str(book1))
print(book1 == book2)
```

Output:

```
420
Built Wealth Like a Boss has 420 pages
True
```

Python internally calls:

```
len(book1) → book1.__len__()
str(book1) → book1.__str__()
book1 == book2 → book1.__eq__(book2)
```

---

# 9. Types of Operations Using Dunder Methods

## Arithmetic Operations

Example methods:

```
__add__()
__sub__()
__mul__()
__truediv__()
```

Example:

```
a + b → __add__()
a - b → __sub__()
```

---

## String Operations

Examples:

```
__str__()
__repr__()
__format__()
```

These control how objects are printed.

---

## Comparison Operations

Examples:

```
__eq__   ==
__lt__   <
__gt__   >
__ne__   !=
```

---

## Iteration Operations

These make objects **iterable**.

Methods used:

```
__iter__()
__next__()
```

Example usage:

```
for item in object:
```

---

# 10. Real World Example – Shopping Cart

Let's design a **Shopping Cart system**.

---

## Cart Class

```python
class Cart:
    def __init__(self):
        self.items = []
```

Cart starts with an **empty list**.

---

## Add Item

```python
def add(self, item):
    self.items.append(item)
```

Example:

```
cart.add("Laptop")
cart.add("Mouse")
```

---

## Remove Item

```python
def remove(self, item):
    if item in self.items:
        self.items.remove(item)
    else:
        print(f"{item} is not in cart")
```

---

## List Items

```python
def list_items(self):
    return self.items
```

Example:

```
print(cart.list_items())
```

Output:

```
['Laptop', 'Mouse']
```

---

# Using Dunder Methods

These make the cart behave like a **built-in container**.

---

## Length of Cart

```python
def __len__(self):
    return len(self.items)
```

Usage:

```
len(cart)
```

---

## Access Item by Index

```python
def __getitem__(self, index):
    return self.items[index]
```

Usage:

```
cart[0]
```

---

## Check Item in Cart

```python
def __contains__(self, item):
    return item in self.items
```

Usage:

```
"Laptop" in cart
```

---

## Iterating Through Cart

```python
def __iter__(self):
    return iter(self.items)
```

Usage:

```python
for item in cart:
    print(item)
```

---

# Full Example

```python
cart = Cart()

cart.add("Laptop")
cart.add("Keyboard")
cart.add("Mouse")

print(len(cart))

print("Laptop" in cart)

for item in cart:
    print(item)
```

Output:

```
3
True
Laptop
Keyboard
Mouse
```

---

# Key Concepts Summary

| Concept            | Meaning                         |
| ------------------ | ------------------------------- |
| Class              | Blueprint                       |
| Object             | Instance of a class             |
| Attribute          | Variable inside class           |
| Instance Attribute | Unique to each object           |
| Class Attribute    | Shared across objects           |
| Method             | Function inside class           |
| Dunder Method      | Special Python behavior methods |

---

# Real Life Analogy (Easy to Remember)

Class → **Blueprint of a house**

Object → **Actual house built from blueprint**

Attributes → **Rooms, color, size**

Methods → **Things house can do (open door, switch light)**

Dunder methods → **Automatic features (door opens when key inserted)**
