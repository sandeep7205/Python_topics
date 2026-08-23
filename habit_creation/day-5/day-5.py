"""

What is a list? it stores the data with ordered indexing which startes from 0
What does a for loop do? execute a data (like loop) to extract each element from it and execute the operation inside it
What does in do? check if a sub elemnt inside an main elemnet
What does % do? it a round divison whcih use exaple to check even numbers 
What is the difference between if and else? the inside code will execute when the if contion true, else is a otional part when if part not execute it cojmes to else PendingDeprecationWarning

"""

developer = {
    "name": "SKM",
    "role": "SDE-1 in PHP",
    "experience": "4.6 years Continuous",
    "python_experience": "Expert in data analysis and automation",
    "currently_learning": "learning the core python, sql ...us for DE",
    "daily_habit": "currently to build my habits to study",
}

for key, value in developer.items():
    print(f"{key}: {value}")

print('\n==============================================================================================\n')

# At 1st i use wrong way as i forgot it but learn by googled and used it  # if(developer.keys() == "python_experience"): #     developer[developer.keys()] = "on the way to learn to get real exprience on DE"


developer['currently_learning'] = "PYTHON, SQL, AWS"
developer.update({'experience': "4.6 years Continuous in core PHP"})
developer.update({'current_day':"Day 5"})
for key, value in developer.items():
    if(key == "python_experience"):
        value = "on the way to learn to get real exprience on DE"
    print(f"{key}: {value}")


print('\n==============================================================================================\n')


# A list of dictionaries representing three developers
developers_list = [
    {
        "name": "Alice Vance",
        "experience": "3 years",
        "role": "Frontend Developer",
    },
    {
        "name": "Bob Chen",
        "experience": "7 years",
        "role": "DevOps Engineer",
    },
    {
        "name": "Clara Smith",
        "experience": "5 years",
        "role": "Data Scientist",
    },
]

for index, developer_data in enumerate(developers_list, start=1):
    print(f"====dev-{index}====")
    for d_key, d_value in developer_data.items():
        print(f"{d_key}: {d_value}") 



"""
Day 5 ✅

I learned: use of dictionary and some of methods

I built: to print multiple dev data

I understood: .update do if key is exist then update else add a new 

I got stuck on: to update a key with new value

I discovered: # At 1st i use wrong way as i forgot it but learn by googled and used it  # if(developer.keys() == "python_experience"): #     developer[developer.keys()] = "on the way to learn to get real exprience on DE"

Time spent: didnot notice but more then 15min

Habit battle today: owned it



For Habit battle today, i spent more then 4 hours doom-scrolling in hole day and thougt to almost skip it but did above 15 minutes after fight with myself as enjoyed the habit journy.

"""