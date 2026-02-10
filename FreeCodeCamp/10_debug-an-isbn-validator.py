# ============================================================
# Debug an ISBN Validator
# ============================================================
#
# The ISBN (International Standard Book Number) is a unique
# identifier assigned to commercial books. It can be either
# 10 or 13 digits long, and the last digit is a check digit
# calculated from the other digits.
#
# Camperbot has tried to build their own ISBN validator.
# However, they have made a few mistakes along the way.
#
# In this lab, you will fix the existing code and make it
# function properly.
#
# ------------------------------------------------------------
# Expected behavior
# ------------------------------------------------------------
# When the user runs the program, it will show the prompt:
#     Enter ISBN and length:
#
# The user can enter the ISBN code they want to validate in
# ISBN,length format.
#
# The ISBN code should not contain hyphens, followed by its
# length (10 or 13), separated by a comma.
#
# Example inputs:
#   1530051126,10    -> ISBN-10
#   9781530051120,13 -> ISBN-13
#
# ------------------------------------------------------------
# How to find the check digit
# ------------------------------------------------------------
# You don't have to know the detailed calculation logic in
# this lab.
#
# The functions below will take care of the calculation:
#   - calculate_check_digit_10
#   - calculate_check_digit_13
#
# These functions return the expected check digit as a string.
#
# ISBN-10:
#   - Check digit can be 0–9 or uppercase 'X'
#
# ISBN-13:
#   - Check digit can be 0–9 only
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
# - You should fix the IndentationError in the current code.
#
# - Even if the user does not enter a comma separated value,
#   the program should handle the IndexError without crashing.
#
# - When the user does not enter a comma separated value,
#   they should see the message:
#       Enter comma-separated values.
#   and the program should terminate.
#
# - Even if the user enters a non-numeric value for the length,
#   the program should handle the ValueError without crashing.
#
# - When the user enters a non-numeric value for the length,
#   they should see the message:
#       Length must be a number.
#   and the program should terminate.
#
# - You should fix the off-by-one error in the validate_isbn
#   function.
#
# - You should fix the TypeError in the current code that
#   occurs when the user enters a valid ISBN code.
#
# - You should fix the IndexError in the current code when
#   the user enters a valid ISBN code.
#
# - Even if the user enters an incorrect ISBN code with
#   characters other than numbers, the program should handle
#   the ValueError without crashing.
#
# - When the user enters an incorrect ISBN code with
#   characters other than numbers, they should see the message:
#       Invalid character was found.
#
# - When the user enters:
#       1530051126,10
#   they should see the message:
#       Valid ISBN Code.
#
# - When the user enters:
#       9781530051120,13
#   they should see the message:
#       Valid ISBN Code.
#
# ------------------------------------------------------------
# Important
# ------------------------------------------------------------
# You will need to comment out the main() call in the global
# space for the tests to run properly.
#
# ------------------------------------------------------------
# Final Output Expectations
# ------------------------------------------------------------
#
# ISBN Code | Length | Message | Example Input
# --------------------------------------------
# Valid | Valid | Valid ISBN Code. | 1530051126,10
#
# Invalid Number | Valid | Invalid ISBN Code. | 1530051125,10
#
# Does not match specified length or left blank | Valid |
# ISBN-10 code should be 10 digits long.
# or
# ISBN-13 code should be 13 digits long.
# | 9781530051120,10 or 1530051126,13
#
# Contains non-numeric characters (except check digit) | Valid |
# Invalid character was found. | 15-0051126,10
#
# Any | Invalid Number | Length should be 10 or 13. |
# 1530051126,9
#
# Any | Contains non-numeric characters or left blank |
# Length must be a number. | 1530051125,A
#
# Not comma-separated | Not comma-separated |
# Enter comma-separated values. | 1530051125
#
# ------------------------------------------------------------
# Manual Test Values
# ------------------------------------------------------------
# Valid ISBN-10:
#   1530051126,10
#   9971502100,10
#   080442957X,10
#
# Valid ISBN-13:
#   9781530051120,13
#   9781947172104,13
# ============================================================

def validate_isbn(isbn, length):

    # 🔹 EARLY CHARACTER VALIDATION
    # This block ensures we reject illegal characters BEFORE doing any other logic.
    # Reason: tests expect "Invalid character was found." immediately
    # if illegal characters (like '-') exist, even if length is correct.

    if length == 10:
        # For ISBN-10:
        # - First 9 characters must be digits
        # - Last character can be a digit OR 'X'
        if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
            print('Invalid character was found.')
            return
    else:  # length == 13
        # For ISBN-13:
        # - ALL characters must be digits
        if not isbn.isdigit():
            print('Invalid character was found.')
            return

    # 🔹 LENGTH VALIDATION
    # This checks whether the ISBN length matches the given length (10 or 13).
    # Even if characters are valid, length mismatch must be handled separately.
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # 🔹 SPLITTING ROLES
    # main_digits → digits used to calculate the check digit
    # given_check_digit → the last character (actual check digit from user input)
    main_digits = isbn[0:(length-1)]
    print(main_digits)

    given_check_digit = isbn[length-1]
    print(given_check_digit)

    # 🔹 CONVERTING MAIN DIGITS TO INTEGERS
    # This is safe now because character validation already happened above.
    main_digits_list = [int(digit) for digit in main_digits]

    # Calculate the check digit from other digits
    # Logic differs for ISBN-10 and ISBN-13
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # 🔹 FINAL COMPARISON
    # If calculated check digit matches the given one → VALID
    # Otherwise → INVALID
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0

    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11

    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)

    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0

    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3

    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10

    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)

    return expected_check_digit


def main():
    user_input = input('Enter ISBN and length: ')

    # 🔹 INPUT FORMAT VALIDATION
    # main() only checks STRUCTURE, not ISBN rules.
    # ISBN logic belongs to validate_isbn().
    if ',' not in user_input:
        print('Enter comma-separated values.')
    else:
        values = user_input.split(',')

        # Length must be numeric
        if not values[1].isnumeric():
            print('Length must be a number.')
        else:
            isbn = values[0]
            length = int(values[1])

            # Length must be either 10 or 13
            if length == 10 or length == 13:
                validate_isbn(isbn, length)
            else:
                print('Length should be 10 or 13.')


if __name__ == "__main__":
    main()