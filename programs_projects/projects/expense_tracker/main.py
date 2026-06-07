import csv

with open("programs_projects\projects\expense_tracker\expense_data_1.csv", "r") as file:
    # reading = csv.reader(file)
    reading = csv.DictReader(file)
    for r in reading:
        print(r)