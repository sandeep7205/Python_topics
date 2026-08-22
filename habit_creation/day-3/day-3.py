"""
Without opening your previous code, answer these:

What is a variable? is a name to to which refer it's value 
What does if do? single conditional statemante
What does elif do? multiple conditional statement withourt having else case
What does else do? having else case if the above if/elf condition not satisfy according to the situation
What does this mean?
experience > 2 and experience < 4  experience means greater then 2 and less then 4

----

Imagine you have:

Python
SQL
AWS
Docker
Git

Without a loop, you'd have to write something separately for each item.

A loop lets you tell Python:

"Take each item, one at a time, and do this." 

- what my understand is we can add it inside an array/list and using for loop we can handelp them one after another untill the last one finish


----

Create a list of 5 technologies/tools you want to learn for Data Engineering.

Then use a for loop to print each one.



"""
tech_lists = ['Program basics', 'Python', 'SQL', 'AWS', 'Docker', 'Git']

for i, tech in tech_lists:
    print(f"I want to learn {tech}")


print("\n----------\n")

for i, tech in enumerate(tech_lists, start=1):
    tech_str = f"{i}. {tech}" if i <= 2 else f"{i}. ..."
    print(tech_str)


print("\n----------\n")

learning_phase = ['Python', 'SQL']
completed_phase = ['Program basics']
for tech in tech_lists:
    process = 'Later'
    if tech in completed_phase:
        process = "completed"
    elif tech in learning_phase: 
        process = "Learning"

    print(f"{tech}  → {process}")





"""
Day 3 ✅

I learned: recalled my self about for looping along with conditions

I built: tech-stack lerning process using loop and conditional statement

I understood:  variable and (experience > 2 and experience < 4)

I got stuck on:forgote about enumerate method nme, did google

One thing I discovered:
single line conditional statement 



my thougt:
today come from office(bring food) but fresh up and did code habit round around 25 , where i didnot start any stopwatch/counter, i just saw the time and start my today's round. now as i finish i will chill with my food and movie

"""
