# Read the file using Python.
header = []
things_dict_summary = {}
date_dict_summary = {}
context = '\n\n'
total = 0
with open("habit_creation/day-10/expenses.csv", 'r') as read_csv:
    get_content = read_csv.readlines()

    # For each line:
    # Remove the newline.
    header = get_content[0].strip().split(',')
    get_content.pop(0)

    for index, content in enumerate(get_content):
        # Separate:
        split_content = content.strip().split(',')
        date = split_content[0]
        things = split_content[1]
        # Convert Amount into a number.
        amount = int(split_content[2])
        # Calculate:
        total += amount 
        context += f"\n{date} {things} → ₹{amount}"
        
        #Print expenses where the amount is greater than ₹300.
        if amount > 300: 
            print(f"{things} → ₹{amount}")

        #Create a things dictionary that dynamically calculates:
        if things not in things_dict_summary:
            things_dict_summary.update({things:amount})
        else:
            things_dict_summary[things] += amount
        
        #Create a date dictionary that dynamically calculates:
        if date not in date_dict_summary:
            date_dict_summary.update({date:amount})
        else:
            date_dict_summary[date] += amount


    context += f"\n-----------------\nTotal → ₹{total}" 
    # print(context)
    # print("\n -----------------\n")


things_summmary = "\n\n\n\n"
for key, value in things_dict_summary.items():
    things_summmary += f"{key} → ₹{value}\n"

# Create a dictionary where the key is the date and the value is the total amount spent that day.
date_summmary = "\n\n\n\n"
for key, value in date_dict_summary.items():
    date_summmary += f"{key} → ₹{value}\n"

# Total amount spent.
print(context, things_summmary, date_summmary)




"""
Day 10 ✅

Memory:
1.What does readlines() return? it returns a list where the elements are eachlines in the respective file
2.Why do we use .strip()?  it erase the whitespace all around incluing newlines 
3.What is a dictionary? it store the data in key value pair
4.What does += 1 do? it increment with 1 x=x+1
5.What does .items() give you? it gives the key & value 
6.What does .append() do? it update the value in list
7.What does a function do? its a block of code which can be reusable

I learned: csv read, split, calculate, show summary

I built: expense summary

I understood: conect to show data in clean way

I got stuck on: how to assign after split

I discovered: to show content in proper way so user can read

Time spent: 40 min aprox (time took to finish) not by forcefully

Habit battle today: not hard to bettel as i was clear to sit at 8pm

"""