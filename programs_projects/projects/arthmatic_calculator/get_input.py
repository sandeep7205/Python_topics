def get_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == 'n':  # Check if user wants to exit
        print("\n🙏 Thank you for using the Ultimate Arithmetic Calculator! 🚀 Have a great day! ✨\n")

        exit()  # Exit the program
    return user_input  # Return input if not exiting
