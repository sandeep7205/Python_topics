"""

1. Variables

What is a variable? it stores different types of values

2. List

What is a list? stores values in ordered index which strts from 0

3. Dictionary

What is a dictionary? store values in terms of key value pair where keys are unique 

4. if

What does if do? it will execute the inside block when the respective condition ture

5. for

What does a for loop do? it execute a itrable value in specific steps manner

6. in

What does in check? check if a selected value inside another value

7. %

What does % return? it returns reminder

8. .items()

What does .items() give you? it giving bboth key and values of dictionary

9. append()

What does .append() do? to add or update a value into list/dict

10. sum()

What does sum() do? it sumation the value inside an array

"""



expenses = [
    {"Date": "Monday", "Category": "Food", "Amount": 250},
    {"Date": "Monday", "Category": "Travel", "Amount": 100},
    {"Date": "Tuesday", "Category": "Food", "Amount": 300},
    {"Date": "Tuesday", "Category": "Shopping", "Amount": 800},
    {"Date": "Wednesday", "Category": "Food", "Amount": 150},
    {"Date": "Thursday", "Category": "Entertainment", "Amount": 450},
    {"Date": "Thursday", "Category": "Travel", "Amount": 450}
]


def sumation_fun(amount,t_amount):
    t_amount += int(amount)
    return t_amount


total_amount = 0
total_food_amount = 0
total_travel_amount = 0
total_entertainment_amount = 0
total_shopping_amount = 0
for expense in expenses:
    total_amount = sumation_fun(expense['Amount'], total_amount)
    if(expense['Category'] == 'Food'):
        total_food_amount = sumation_fun(expense['Amount'], total_food_amount)
    if(expense['Category'] == 'Travel'):
        total_travel_amount = sumation_fun(expense['Amount'], total_travel_amount)
    if(expense['Category'] == 'Entertainment'):
        total_entertainment_amount = sumation_fun(expense['Amount'], total_entertainment_amount)
    if(expense['Category'] == 'Shopping'):
        total_shopping_amount = sumation_fun(expense['Amount'], total_shopping_amount)
print(f"Total expenses: ₹{total_amount}")
print(f"Food expenses: ₹{total_food_amount}")
print(f"Travel expenses: ₹{total_travel_amount}")
print(f"Entertainment expenses: ₹{total_entertainment_amount}")
print(f"Shopping expenses: ₹{total_shopping_amount}")


"""

A function is: resuable code
My function takes: amount nd totalamout
My function returns: amount sum



I learned: function

I built: function takes  amount nd totalamout and returns amount sum

I understood: function 

I got stuck on: in sumation_fun

I discovered: having diffult value or not having in function paramerts

Time spent: not know

Habit battle today: ggreat