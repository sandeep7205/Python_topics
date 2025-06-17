import calculator_world


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

            return calculator_world.calculator_world(number_1_input, number_2_input, process_input)
    else:
        print(f"❌ Invalid input! Please enter the  valid input form given list")
        return process_input_fn(result, number_1_input, number_2_input)
