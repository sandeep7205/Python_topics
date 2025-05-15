# making of a simple Arthmatic Calculator



# try-4
# -----
import re
import operator

# Define supported operators
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow
}
operator_prompt = "\n🛠 Choose an operation:\n" + " ".join([f"[{op}]" for op in operators.keys()])

def show_welcome():
    print("\n🔢 Welcome to the Ultimate Arithmetic Calculator! 🔢\n"
          "✨ Perform basic math operations.\n"
          "✨ Enter valid numbers to start!\n"
          "✨ Type 'Ac' for new calculation or 'N' to exit.\n")

def calculator_world(number_1_input = 0, number_2_input = 0, process_input = '', operator_input = ''):
    operator_list = list(operators.keys())  # Valid operators
    pattern = r"^[+-]?(?:\d+|\d*\.\d+)$"  # Regex to validate numbers

    #opeartor input
    if(operator_input == ''):
        operator_input = get_input(operator_prompt + "\n🛠 Enter the operator (or 'N' to exit): ")

    # Validate opeartor
    if (operator_input in operator_list):
        if (process_input == 'y'):
            number_1_input = str(number_1_input)
            print(f"\n🔢 Now the FIRST number: {round(float(number_1_input),2)}")
        else:
            # User inputs
            number_1_input = get_input("\n🔢 Enter the FIRST number (or 'N' to exit): ")

        # Validate first number
        if not re.fullmatch(pattern, number_1_input):
            print("❌ Oops! That doesn't look like a number. Please enter a valid numeric value.")
            return calculator_world(0, 0, '', operator_input)
        else:
            number_2_input = get_input("\n🔢 Enter the SECOND number (or 'N' to exit): ")
            # Validate second number
            if not re.fullmatch(pattern, number_2_input):
                print("❌ Oops! That doesn't look like a number. Please enter a valid numeric value.")
                return calculator_world(number_1_input, 0, 'y', operator_input)
            else:
                if(operator_input == '/' and (float(number_2_input) == 0.0)):
                    print("❌ Error: Division by zero is not allowed! Please enter a different number.")
                    return calculator_world(number_1_input, 0, 'y', operator_input)
                else:
                    return  calculation_function(number_1_input, number_2_input, operator_input)
    else:
        print(f"❌ Invalid choice! Please select a valid operator from: {operator_list}")
        return calculator_world(number_1_input, number_2_input, process_input)



def calculation_function(number_1_input, number_2_input, operator_input):

    # Convert valid inputs to float
    number_1_input = float(number_1_input)
    number_2_input = float(number_2_input)

    #evaluate the operator with the input values
    result = operators[operator_input](number_1_input, number_2_input)
    print(f"\n✅ Calculation Complete! 🎉\nResult: {number_1_input} {operator_input} {number_2_input} = {round(result, 2)}\n")
    return process_input_fn(result)

def process_input_fn(result = 0, number_1_input = 0 , number_2_input = 0, process_input = ''):
    process_input_list = ['y', 'n', 'ac'] # valid next steps

    process_input = input(
    "\nWhat would you like to do next?"
    "\n📌 Continue with the result? → Press [Y] or [y]"
    "\n📌 Start a new calculation? → Press [Ac] or [ac]"
    "\n📌 Exit the calculator? → Press [N] or [n]"
    "\n\nYour choice: "
    ).lower()

    if (process_input in process_input_list):

        if (process_input == 'n'):
            print("\n🙏 Thank you for using the Ultimate Arithmetic Calculator! 🚀 Have a great day! ✨\n")
            exit()
        else:
            print(f"\nuser's next step: " + process_input + "\n")
            if (process_input == 'ac'):
                show_welcome()
                result = 0
            else:
                number_1_input = result

            return calculator_world(number_1_input, number_2_input, process_input)
    else:
        print(f"❌ Invalid input! Please enter the  valid input form given list")
        return process_input_fn(result, number_1_input, number_2_input)

def get_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == 'n':  # Check if user wants to exit
        print("\n🙏 Thank you for using the Ultimate Arithmetic Calculator! 🚀 Have a great day! ✨\n")

        exit()  # Exit the program
    return user_input  # Return input if not exiting


def main():
    show_welcome()
    calculator_world()

if __name__ == "__main__":
    main()





















































"""
# try-1
# -----
operator_list = ['+', '-', '*', '/']
operator_input = input(f"Choose the operator for calculation between two numbers {operator_list}: ")
result = 0
try:
    index_check = operator_list.index(operator_input)
    number_1_input = float(input("Enter first the number: "))
    number_2_input = float(input("Enter second the number: "))

    if (operator_input == '+'):
        result = number_1_input + number_2_input 
    elif (operator_input == '-'):
        result =number_1_input: number_2_input
    elif (operator_input == '*'):
        result = number_1_input * number_2_input
    elif (operator_input == '/'):
        result = number_1_input / number_2_input
    else:
        print("Select valid operator")
    
    print(result)
except ValueError:
    print(f"Select operator for calculation form list {operator_list}")




# try-2
# -----
operator_list = ['+', '-', '*', '/']
operator_input = input(f"Choose the operator for calculation between two numbers {operator_list}: ")
result = 0
try:
    # operator_list.index(operator_input)
    number_1_input = float(input("Enter first the number: "))
    number_2_input = float(input("Enter second the number: "))

    result = eval(f"{number_1_input} {operator_input} {number_2_input}")

    print(f"{number_1_input} {operator_input} {number_2_input} = {result}")
except ValueError:
    print(f"Select operator for calculation form list {operator_list}")




# try-3
# -----
import re
def calculation_function():
    operator_list = ['+', '-', '*', '/'] # valid operators
    pattern = r"^[+-]?(?:\d+|\d*\.\d+)$"  # Regex to validate numbers
    #opeartor input
    operator_input = input(f"Choose the operator for calculation between two numbers {operator_list}: ")
    result = 0

    # Validate opeartor
    if (operator_input in operator_list):

        # User inputs
        number_1_input = input("Enter first the number: ")

        # Validate first number
        if not re.fullmatch(pattern, number_1_input):
            print("❌ Invalid first input! Please enter only numbers.")
        else:
            number_2_input = input("Enter second the number: ")

            # Validate second number
            if not re.fullmatch(pattern, number_2_input):
                print("❌ Invalid second input! Please enter only numbers.")
            else:
                # Convert valid inputs to float
                number_1_input = float(number_1_input)
                number_2_input = float(number_2_input)

                result = eval(f"{number_1_input} {operator_input} {number_2_input}")
                print(f"{number_1_input} {operator_input} {number_2_input} = {round(result, 2)}")

                # Pr
    else:
        print(f"❌ Invalid operator input! Please enter the operator form given list {operator_list}")

print("\nWelcome to the Calculator World!\n\n")
calculation_function()

"""