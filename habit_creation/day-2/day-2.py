"""
Without looking at yesterday's code, answer:

What is a variable? it's a name where a value can be stored.
What is a str? anything inside single/double quote mark as string
What is a float? number having decimal values like 23.45
What is a bool? it can be either true or false
What does = do? assignment operator

---------

Think about this real-life situation:

You have 3.8 years of experience.

You want Python to make a decision:

If experience is less than 2 → "Junior"
If experience is between 2 and 4 → "Mid-level"
If experience is greater than 4 → "Senior"

That's exactly the kind of problem if / elif / else solves.



--------

"""
desgignation = ""

exprience = 3.8
exprience = 0
exprience = 1.9
exprience = 2.9
exprience = 4
learning_DE = True

if learning_DE:
    if exprience > 4:
        desgignation = "Senior"
    elif exprience > 2 and exprience <= 4:
        desgignation = "Mid-level"
    elif exprience < 2:
        desgignation = "Junior"
    else:
        desgignation = "No Desgignation"

    print(f"I have {desgignation} desgignation with {exprience} years exprience in DE field")
else:
    print(f"I have no exprience in DE field")
    

# the above is a conditional section where we have exp levels in which we can desginate them




# # # Day 2 ✅

# # I learned: Contional statement if/elifelse

# # I built:
# # a exp levels report in which we know the person's designation by their years of exp.

# # I tested:
# # PS D:\habit_creation/day-2/day-2.py
# # I have Mid-level with 3.8 years exprience
# # PS D:\habit_creation/day-2/day-2.py
# # I have No Desgignation with 0 years exprience
# # PS D:\habit_creation/day-2/day-2.py
# # I have No Desgignation with 1.9 years exprience
# # PS D:\habit_creation/day-2/day-2.py
# # I have Junior with 1.9 years exprience
# # PS D:\habit_creation/day-2/day-2.py
# # I have Senior desgignation with 6.9 years exprience
# # PS D:\habit_creation/day-2/day-2.py
# # I have Mid-level desgignation with 2.9 years exprience
# # PS D:\habit_creation/day-2/day-2.py
# # I have Senior desgignation with 6.9 years exprience in DE field
# # PS D:\habit_creation/day-2/day-2.py
# # I have no exprience in DE field

# # I got stuck on:
# # got confuse elif exprience > 2 and exprience < 4: where i added 2<exprience<4:

# # One thing I understand better:
# # use of conditional



# today i am doing this after coming from office- fresh up- put the food aside and extertainemt (as after complete these will be my rewaord to myself)

# i was rusing for time as i set the time 15min backword to 0min, while writing code, my mind got sifts, i try to control (som hwere like in exam )