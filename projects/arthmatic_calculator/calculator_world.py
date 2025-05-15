import re
import operators_list
import get_input
import calculation_function


operator_prompt = "\n🛠 Choose an operation:\n" + " ".join([f"[{op}]" for op in operators_list.operators.keys()])

def calculator_world(number_1_input = 0, number_2_input = 0, process_input = '', operator_input = ''):
    operator_list = list(operators_list.operators.keys())  # Valid operators
    pattern = r"^[+-]?(?:\d+|\d*\.\d+)$"  # Regex to validate numbers

    #opeartor input
    if(operator_input == ''):
        operator_input = get_input.get_input(operator_prompt + "\n🛠 Enter the operator (or 'N' to exit): ")

    # Validate opeartor
    if (operator_input in operator_list):
        if (process_input == 'y'):
            number_1_input = str(number_1_input)
            print(f"\n🔢 Now the FIRST number: {round(float(number_1_input),2)}")
        else:
            # User inputs
            number_1_input = get_input.get_input("\n🔢 Enter the FIRST number (or 'N' to exit): ")

        # Validate first number
        if not re.fullmatch(pattern, number_1_input):
            print("❌ Oops! That doesn't look like a number. Please enter a valid numeric value.")
            return calculator_world(0, 0, '', operator_input)
        else:
            number_2_input = get_input.get_input("\n🔢 Enter the SECOND number (or 'N' to exit): ")
            # Validate second number
            if not re.fullmatch(pattern, number_2_input):
                print("❌ Oops! That doesn't look like a number. Please enter a valid numeric value.")
                return calculator_world(number_1_input, 0, 'y', operator_input)
            else:
                if(operator_input == '/' and (float(number_2_input) == 0.0)):
                    print("❌ Error: Division by zero is not allowed! Please enter a different number.")
                    return calculator_world(number_1_input, 0, 'y', operator_input)
                else:
                    return  calculation_function.calculation_function(number_1_input, number_2_input, operator_input)
    else:
        print(f"❌ Invalid choice! Please select a valid operator from: {operator_list}")
        return calculator_world(number_1_input, number_2_input, process_input)

