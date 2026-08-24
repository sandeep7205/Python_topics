"""
What is a dictionary? it a data type which having key value pair without duplicacy
What does .items() give you? gives to extract or excess both the keys and value
What does a for loop do? to extrat the elments from list/set/dicionary
What does in do? check if an elment is inside of an elemnt
What does % do? its a operator who retuen divsor


"""
# Create a list of dictionaries representing expenses:
expenses = [
    {"Date": "Monday", "Category": "Food", "Amount": 250},
    {"Date": "Monday", "Category": "Travel", "Amount": 100},
    {"Date": "Tuesday", "Category": "Food", "Amount": 300},
    {"Date": "Tuesday", "Category": "Shopping", "Amount": 800},
    {"Date": "Wednesday", "Category": "Food", "Amount": 150},
    {"Date": "Thursday", "Category": "Entertainment", "Amount": 450}
]



total_amount = 0
total_food_amount = []
for expense in expenses:
    total_amount += int(expense['Amount'])
    print(f"{expense['Category']} → {expense['Amount']}") #Use a for loop to print every expense.
    if (expense['Category'] == 'Food'):
        total_food_amount.append(int(expense['Amount']))

print(f"\n Total Amount = {total_amount}")  #Calculate the total amount of all expenses.
print(f"\n Total Food Amount = {sum(total_food_amount)} \n")  #Calculate the total amount spent on Food only.


print('\n==============================================================================================\n')

for expense in expenses:
    if(int(expense['Amount']) > 200): #Use a condition to print only expenses greater than ₹200.
        print(f"{expense['Category']} → {expense['Amount']}")





"""
Day 6 ✅

I learned: extract data and calculate

I built: expense system

I understood: loop, in, item

I got stuck on:  i use php code (total_food_amount[] = int(expense['Amount'])) instead of append

I discovered: different types of sum

Time spent: 23 min

Energy today: Low / Medium / High  Medium

Habit battle today: owned
"""
