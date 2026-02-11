# ============================================================
# Build a Travel Weather Planner
# ============================================================
#
# For this lab, you will use conditional statements to determine
# whether commuting is possible based on the weather, the
# distance to travel, and the availability of a vehicle.
#
# ------------------------------------------------------------
# Objective
# ------------------------------------------------------------
# Fulfill the user stories below and get all the tests to pass
# to complete the lab.
#
# ------------------------------------------------------------
# Required Variables
# ------------------------------------------------------------
#
# You should create the following variables:
#
# - distance_mi
#     (a number representing the distance to travel in miles)
#
# - is_raining
#     (a boolean representing if the user is currently
#      experiencing rainy weather)
#
# - has_bike
#     (a boolean representing if the user has a bicycle)
#
# - has_car
#     (a boolean representing if the user has a car)
#
# - has_ride_share_app
#     (a boolean representing if the user has an app that
#      allows them to request a ride)
#
# ------------------------------------------------------------
# Conditional Logic Requirements
# ------------------------------------------------------------
#
# - You should use conditional statements to determine whether
#   commuting is possible based on the values of these variables.
#
# - You should use if, elif, and else statements to evaluate
#   the distance categories in ascending order.
#
# ------------------------------------------------------------
# Distance Conditions
# ------------------------------------------------------------
#
# - If distance_mi is a falsy value:
#       You should print False.
#
# - If the distance is less than or equal to 1 mile:
#       You should print True only if it is not raining.
#       Otherwise, you should print False.
#
# - If the distance is greater than 1 mile and less than or
#   equal to 6 miles:
#       You should print True only if the person has a bike
#       and it is not raining.
#       Otherwise, you should print False.
#
# - If the distance is greater than 6 miles:
#       You should print True if the person has a car or has
#       a ride-share app.
#       Otherwise, you should print False.
#
# ------------------------------------------------------------
# Controls
# ------------------------------------------------------------
# Run the Tests (Ctrl + Enter)
# Reset this lesson
# Get Help
#
# ------------------------------------------------------------
# Tests
# ------------------------------------------------------------
#
# Waiting: 1. You should have a variable named distance_mi.
#
# Waiting: 2. You should assign a number to your distance_mi
#             variable.
#
# Waiting: 3. You should have a variable named is_raining.
#
# Waiting: 4. You should assign a boolean to your is_raining
#             variable.
#
# Waiting: 5. You should have a variable named has_bike.
#
# Waiting: 6. You should assign a boolean to your has_bike
#             variable.
#
# Waiting: 7. You should have a variable named has_car.
#
# Waiting: 8. You should assign a boolean to your has_car
#             variable.
#
# Waiting: 9. You should have a variable named
#             has_ride_share_app.
#
# Waiting: 10. You should assign a boolean to your
#              has_ride_share_app variable.
#
# Waiting: 11. You should use at least one if statement.
#
# Waiting: 12. You should use at least one elif branch in your
#              program.
#
# Waiting: 13. You should use at least one boolean operator
#              (and, or, or not) in your code.
#
# Waiting: 14. You should use the print() function to display
#              the result.
#
# Waiting: 15. When the distance is 1 mile or less and it is
#              not raining, the program should print True.
#
# Waiting: 16. When the distance is 1 mile or less and it is
#              raining, the program should print False.
#
# Waiting: 17. When the distance is between 1 mile (excluded)
#              and 6 miles (included), and it is raining with
#              no bike, the program should print False.
#
# Waiting: 18. When the distance is between 1 mile (excluded)
#              and 6 miles (included), it is not raining but
#              no bike is available, the program should print
#              False.
#
# Waiting: 19. When the distance is between 1 mile (excluded)
#              and 6 miles (included), a bike is available,
#              and it is not raining, the program should print
#              True.
#
# Waiting: 20. When the distance is greater than 6 miles and
#              a ride share app is available, the program
#              should print True.
#
# Waiting: 21. When the distance is greater than 6 miles and
#              a car is available, the program should print
#              True.
#
# Waiting: 22. When the distance is greater than 6 miles and
#              no car nor a ride share app is available, the
#              program should print False.
#
# ============================================================

# ------------------------------------------------------------
# Required Variables
# ------------------------------------------------------------

# Distance to travel in miles (must be a number)
distance_mi = 0

# Weather condition (boolean)
is_raining = False

# Transportation availability (booleans)
has_bike = True
has_car = False
has_ride_share_app = False

# ------------------------------------------------------------
# Commuting Logic
# ------------------------------------------------------------
# Rules:
# 1. If distance is falsy (0), commuting is not possible → False
# 2. If distance ≤ 1 mile:
#       True only if it is NOT raining
# 3. If 1 < distance ≤ 6 miles:
#       True only if the user has a bike AND it is NOT raining
# 4. If distance > 6 miles:
#       True if the user has a car OR ride-share app
# ------------------------------------------------------------

if not distance_mi:
    # Distance is falsy (0 or equivalent)
    print(False)

elif distance_mi <= 1:
    # Walking distance
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi <= 6:
    # Medium distance — bike required and no rain
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

else:
    # Long distance — car or ride-share required
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)

# ============================================================
# Example Test Scenarios
# ============================================================
#
# Scenario 1:
# distance_mi = 1
# is_raining = False
# → Output: True
#
# Scenario 2:
# distance_mi = 1
# is_raining = True
# → Output: False
#
# Scenario 3:
# distance_mi = 5
# is_raining = True
# has_bike = False
# → Output: False
#
# Scenario 4:
# distance_mi = 5
# is_raining = False
# has_bike = True
# → Output: True
#
# Scenario 5:
# distance_mi = 10
# has_car = True
# → Output: True
#
# Scenario 6:
# distance_mi = 10
# has_car = False
# has_ride_share_app = False
# → Output: False
#
# ============================================================
