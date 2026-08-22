"""
Without looking at your previous code, answer:

What is a list? set of array who can carry different data types value along with it's index
What does a for loop do? it extract an array to get every value of of it
What does if do? the code will execute if the contion satisfy
What does in do? verify if an value exist inside another value 
What does enumerate() give you? bothe the index and it's respective value of an array



"""

tech_list = ['Python', 'SQL', 'AWS', 'Docker', 'Git', 'JavaScript', 'HTML', 'CSS']
DE_tech_list = ['Python', 'SQL', 'AWS', 'Docker']
lerning_list = ['Python', 'SQL']
DE_str = "Data Engineering technologies:\n" 
for techs in tech_list:
    if techs in DE_tech_list:
        if techs in lerning_list:
            DE_str += f"\n{techs} -> Learning" 
        else:
            DE_str += f"\n{techs} -> Later" 
print(DE_str)

print("\n===========================================================\n")

num_list = [5, 12, 3, 20, 8, 15, 2]
boundry = 10
for num in num_list:
    if num > boundry:
        print(f"{num} is greater the {boundry}") 

print("\n===========================================================\n")

for num in num_list:
    if num % 2 == 0:
        print(f"{num} is a even number") 

"""
Day 4 ✅

I learned: revise the loop & condition

I built: techstack learning map, check the greater than , evn nujmbers

I understood: recall the string concatination 

I got stuck on: none today

I discovered: recalling imedeatly the previous days taks

Time spent: 13 min (got completed the assigned taks) and writing the day-4 note




today was my holiday, so i try a small experiment (local llm store in pendrive and run in win/ubuntu/linux/mac), then did some laudry, then show some moie and chill no regerts then came at same time like yesterday for task and now i eat and chill again