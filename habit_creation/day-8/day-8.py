"""
What is a variable? it represt a value
What is a list? it conains multiple elemnts with ordered index starts from 0
What is a dictionary? it contains key value pair
What does a for loop do? go thorugh each element of the itrable and ececute inside loop body accordingly
What does a function do? use to resue a similar kind of operation
What does .append() do? add/updte the elemnt into list
What does .items() do? gives key & value
What does sum() do? sumation of array
"""



# # 1. Open the file
# file_open = open("habit_creation\day-8\learning.txt", "r") 

# # 2. Read the contents
# print(file_open.read())
# print("\n\n==========================================================================================\n\n")

# file_open = open("habit_creation\day-8\learning.txt", "r") 

# # 3. Read it line by line
# print(file_open.readline())
# print(file_open.readline())
# print(file_open.readline())
# print(file_open.readline())
# print(file_open.readline())
# print(file_open.readline())
# print(file_open.readline())



# 4. Count something
# After reading the file, determine:
# How many lines are in the file?
# with open("habit_creation\day-8\learning.txt", "r")  as f:
#     # print(f.read())
#     # print("Numer of lines:", sum([1 for line in f]))
#     print("Numer of lines:", len(f.readlines()))




# ---------------------------------------------------------------------------------------------------------


"""
What does open() do? open a file from given path
What does .read() do? it reads the file conent and shows
What does .readline() do? shows only one line
What does .readlines() give you? gives all lines are there in file 
"""





# Read the file using readlines().
# Store the result in a variable.
# Print that variable.
# Print its len().
# Look carefully at the output.

# with open("habit_creation/day-8/learning.txt", "r") as f:
#     content = f.readlines()
#     print(f"\n\n{content}")
#     print(f"\n\nNumer of lines: {len(content)}\n\n")

# I think it's a list but having \n
# ['Python (pandas, NumPy, data structures)\n', 'SQL (joins, window functions, query optimization)\n', 'Data Engineering (pipelines, orchestration with Airflow)\n', 'AWS (S3, EC2, Redshift, Lambda basics)\n', 'ETL processes (extract, transform, load workflows)\n', 'Git & GitHub (version control, collaboration)\n', 'Docker (containers, basic orchestration)']
# Numer of lines: 7



#Count how many times Food appears.

with open("habit_creation/day-8/expenses.txt", 'r') as e:
    exp_content = e.readlines()
    f_cnt = 0
    t_cnt = 0
    s_cnt = 0
    e_cnt = 0
    for ec in exp_content:
        ec= ec.strip()
        if ec == "Food":
            f_cnt+=1   
        elif ec == "Travel":
            t_cnt+=1   
        elif ec == "Shopping":
            s_cnt+=1   
        elif ec == "Entertainment":
            e_cnt+=1   

    print(f"Food appears {f_cnt} times.")
    print(f"Travel appears {t_cnt} times.")
    print(f"Shopping appears {s_cnt} times.")
    print(f"Entertainment appears {e_cnt} times.")




"""
Day 8 ✅

I learned: open, read, file

I built: file read and do opeation 

I understood: different read type

I got stuck on: diff betwwen readlines & list

I discovered: strip()

Time spent: 36

Habit battle today: fight with my mind to get the work done first then food