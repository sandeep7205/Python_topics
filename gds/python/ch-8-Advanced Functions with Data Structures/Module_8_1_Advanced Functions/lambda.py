# Suppose we have a list of tuples representing people with age and name

people = [('Alice', 32), ('Bob', 15), ('Charlie', 20), ('David', 10)]

# We can use a lambda function to sort by age


sorted_people = sorted(people, key=lambda person: person[1])


# This will sort the list by the second element in each tuple, which is age

print(sorted_people)