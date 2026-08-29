def count_function(input_list = []):
    # Create an empty dictionary.
    count_dict = {}
    if len(input_list) > 0:
        for input_value in input_list:
            # Remove whitespace/newlines.
            input_value = input_value.strip()
            # Use the category as the dictionary key.
            if input_value not in count_dict:
                count_dict.update({input_value:1})
            else:
                # Count how many times each category appears.
                count_dict[input_value] += 1
                # count_dict.update({input_value: count_dict[input_value]}) //the dictionary has already been updated. so doesn't add anything.
    return count_dict



count_output = {}
# Open the file.
with open("habit_creation/day-9/expenses.txt", "r") as expense_data:
    # Read each line.
    expense_list = expense_data.readlines()
    if len(expense_list) > 0:
        count_output = count_function(expense_list)
    else:
        print("\nNo Records Found with in the File\n")
# Print the final dictionary.\
if count_output:
    summary =  f"\nCategory Summary\n----------------\n"
    for key, value in count_output.items():
        summary += f"{key}: {value}\n"
    print(summary)


"""
Day 9 ✅

Memory:
1. What does readlines() return? return the lines in the file as elemts inside a list, it retunrn an array 
2. Why did we use .strip()? it trimes the whitespace from both side
3. What is a dictionary? it stores the emelents in key value pair, where keys are unique
4. How do you access a dictionary value using a key? dict['keyname'] which give us the value
5. How do you add a new key/value pair to a dictionary? dict.update({key:value}) but the key shuld not be there in the dict else it will update
6. What does .items() give you? it give both keys and values 
7. What does += 1 do? it is same as x = x+ 1 , increment with 1




I learned: how to make dynamic script in python

I built: dynamic expense summary script

I understood:How the structure works

I got stuck on: in counting and update the expenses if exist but i made it after retries, althouhg i googled about .update 

I discovered: adding validation so the script works without any stucks, i can add try catch to improve

Time spent: more then 30 min i gusses

Habit battle today: although holiday today but not much i battled as i had alreay decided to as the same 8pm as i do everyday

"""