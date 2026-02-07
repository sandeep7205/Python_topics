# ============================================================
# File Name: workshop-report-card-printer.py
# ============================================================
#
# Description:
# This script demonstrates variable declaration and basic
# type checking in Python. It prints student-related details
# along with their data types.
#
# ============================================================

# Student name (string)
name = 'Alice'
print(name, type(name))

# Student status (boolean)
is_student = True
print(is_student, type(is_student))

# Student age (integer)
age = 20
print(age, type(age))

# Student score (float)
score = 80.5

# Check if score is a float
print(isinstance(score, float))

# Print score value and its type
print(score, type(score))
