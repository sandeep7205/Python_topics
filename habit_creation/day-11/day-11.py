"""
Day 11 ✅

Memory:
1.What does readlines() return? it return the each lines element wise inside a list 
2.Why did we use .strip()? it erase the erase the whitespace from arround along with newline
3.What does .split(',') do? it splits a string from given point else using space into a list
4.Why did we use int() on Amount? converts into interger value
5.What is a dictionary? it store the data in key value pair and keys are unique
6.What does .items() give you? it extracts the key and value from dictionary
7.What does += do? s+=y is same as s = s+ y



I learned: start to under stand csv module

I built: expense calculation using csv module 

I understood: littil bit between reader & dictreader

I got stuck on: how to calculate easyly reader

I discovered:  then discover dictreader

Time spent: around 40min

Habit battle today: start lately 5min, was seeing yt. didnot force , just put a reminder to my mind and switched to task


"""

# 1. Import Python's CSV module
import csv

# 2. Open your CSV file
with open("habit_creation/day-11/expenses.csv", "r", newline='') as csvfile:
    # 3. Read the CSV using the CSV module
    # Challenge 1 — Understand the row [What type is this row?]
    rows = csv.reader(csvfile) # data type -> list

    # Get the header row as a list
    header = next(rows)
    print(f"\nHeader: {header}\n")
    # 4. Print each row
    for row in rows:
        print(row, " || Type ->", type(row)) 



print("\n\n================================================\n")



total_amount = 0
cat_dict_amount = {} 
# 2. Open your CSV file
with open("habit_creation/day-11/expenses.csv", "r", newline='') as csvfile:
    # 3. Read the CSV using the CSV module
    #Challenge 1 — Understand the row [What type is this row?]
    dict_rows = csv.DictReader(csvfile) # data type -> dict

    # Get headers via the fieldnames attribute
    header = dict_rows.fieldnames
    print(f"\nHeader: {header}\n")
    
    # 4. Print each row
    for d_row in dict_rows:
        print(d_row, " || Type ->", type(d_row)) 
        amount = int(d_row['Amount'])
        # Challenge 2 — Calculate the total
        total_amount += amount

        # Challenge 3 — Category summary
        if d_row['Category'] not in cat_dict_amount:
           cat_dict_amount.update({d_row['Category']:amount}) 
        else:
            cat_dict_amount[d_row['Category']] += amount

        
 # Challenge 3 — Category summary
category_summmary = ""
for key, value in cat_dict_amount.items():
    category_summmary += f"{key} → ₹{value}\n"

print(f"\n-----------------\n{category_summmary}")

print(f"-----------------\nTotal → ₹{total_amount}\n-----------------\n")