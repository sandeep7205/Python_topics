import process_input
import operators_list

def calculation_function(number_1_input, number_2_input, operator_input):

    # Convert valid inputs to float
    number_1_input = float(number_1_input)
    number_2_input = float(number_2_input)

    #evaluate the operator with the input values
    result = operators_list.operators[operator_input](number_1_input, number_2_input)
    print(f"\n✅ Calculation Complete! 🎉\nResult: {number_1_input} {operator_input} {number_2_input} = {round(result, 2)}\n")
    return process_input.process_input_fn(result)
