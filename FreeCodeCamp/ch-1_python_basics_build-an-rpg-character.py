# ============================================================
# Build an RPG Character
# ============================================================
#
# In this lab you will practice the basics of Python by building
# a small app that creates a character for an RPG adventure.
#
# ------------------------------------------------------------
# Objective
# ------------------------------------------------------------
# Fulfill the user stories below and get all the tests to pass
# to complete the lab.
#
# ------------------------------------------------------------
# User Stories
# ------------------------------------------------------------
#
# - You should have a function named create_character.
#
# - The function should accept, in order:
#     - a character name
#     - strength
#     - intelligence
#     - charisma
#
# ------------------------------------------------------------
# Character Name Validation
# ------------------------------------------------------------
#
# - If the character name is not a string, the function should
#   return:
#       The character name should be a string.
#
# - If the character name is an empty string, the function
#   should return:
#       The character should have a name.
#
# - If the character name is longer than 10 characters, the
#   function should return:
#       The character name is too long.
#
# - If the character name contains spaces, the function should
#   return:
#       The character name should not contain spaces.
#
# ------------------------------------------------------------
# Stats Validation
# ------------------------------------------------------------
#
# - If one or more stats are not integers, the function should
#   return:
#       All stats should be integers.
#
# - If one or more stats are less than 1, the function should
#   return:
#       All stats should be no less than 1.
#
# - If one or more stats are more than 4, the function should
#   return:
#       All stats should be no more than 4.
#
# - If the sum of all stats is different than 7, the function
#   should return:
#       The character should start with 7 points.
#
# ------------------------------------------------------------
# Successful Character Creation
# ------------------------------------------------------------
#
# - If all values pass the verification, the function should
#   return a string with four lines:
#
#   - Line 1:
#       The character name
#
#   - Lines 2–4:
#       Each line should start with the stat abbreviation
#       (in this order):
#           STR
#           INT
#           CHA
#
#       Followed by:
#           - a space
#           - a number of full dots (●) equal to the stat value
#           - a number of empty dots (○) to reach 10 total dots
#
#   Example:
#       If the value of strength is 3, there must be:
#           ●●●○○○○○○○
#
#   The dots are given in the editor.
#
# ------------------------------------------------------------
# Example Output
# ------------------------------------------------------------
#
# The string that should be returned by:
#     create_character('ren', 4, 2, 1)
#
# ren
# STR ●●●●○○○○○○
# INT ●●○○○○○○○○
# CHA ●○○○○○○○○○
#
# ------------------------------------------------------------
# Important Note
# ------------------------------------------------------------
#
# While "str" and "int" are common abbreviations for the stats,
# remember that those are reserved keywords in Python and
# should not be used as variable names.
#
# ------------------------------------------------------------
# Tests
# ------------------------------------------------------------
#
# Waiting: 1. You should have a function named create_character.
#
# Waiting: 2. When create_character is called with a first
#             argument that is not a string it should return:
#             The character name should be a string.
#
# Waiting: 3. When create_character is called with a first
#             argument that is an empty string it should return:
#             The character should have a name.
#
# Waiting: 4. When create_character is called with a first
#             argument that is longer than 10 characters it
#             should return:
#             The character name is too long.
#
# Waiting: 5. The create_character function should not say that
#             the character is too long when it's not longer
#             than 10 characters.
#
# Waiting: 6. When create_character is called with a first
#             argument that contains a space it should return:
#             The character name should not contain spaces.
#
# Waiting: 7. When create_character is called with a second,
#             third or fourth argument that is not an integer
#             it should return:
#             All stats should be integers.
#
# Waiting: 8. When create_character is called with a second,
#             third or fourth argument that is lower than 1
#             it should return:
#             All stats should be no less than 1.
#
# Waiting: 9. When create_character is called with a second,
#             third or fourth argument that is higher than 4
#             it should return:
#             All stats should be no more than 4.
#
# Waiting: 10. When create_character is called with a second,
#              third or fourth argument that do not sum to 7
#              it should return:
#              The character should start with 7 points.
#
# Waiting: 11. create_character('ren', 4, 2, 1) should return:
#              ren\nSTR ●●●●○○○○○○
#              \nINT ●●○○○○○○○○
#              \nCHA ●○○○○○○○○○.
#
# Waiting: 12. When create_character is called with valid
#              values it should output the character stats
#              as required.
#
# ============================================================





full_dot = '●'
empty_dot = '○'

def create_character(name,strength,intelligence,charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    elif len(name) == 0:
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif name.count(" ") > 0:
        return 'The character name should not contain spaces'

    if (not isinstance(strength, int)) or (not isinstance(intelligence, int)) or (not isinstance(charisma, int)):
        return 'All stats should be integers'
    elif (strength < 1) or (intelligence < 1) or (charisma < 1):
        return 'All stats should be no less than 1'
    elif (strength > 4) or (intelligence > 4) or (charisma > 4):
        return 'All stats should be no more than 4'
    elif (strength + intelligence + charisma) != 7:
        return 'The character should start with 7 points'

    return (
        f"{name}\n"
        f"STR {(full_dot * strength) + (empty_dot * (10 - strength))}\n"
        f"INT {(full_dot * intelligence) + (empty_dot * (10 - intelligence))}\n"
        f"CHA {(full_dot * charisma) + (empty_dot * (10 - charisma))}"
    ) 
print(create_character('ren', 4, 2, 1))