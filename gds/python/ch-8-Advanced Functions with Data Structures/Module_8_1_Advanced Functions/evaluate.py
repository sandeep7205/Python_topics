# User input simulation for a number


user_input = '7'

# Building the expression to calculate the square of the number
expression = f"{user_input} ** 2"


print(type(expression))
# Evaluating the expression
result = eval(expression)


# Print out the result
print(f"The square of {user_input} is {result}")
