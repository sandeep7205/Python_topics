# Define a list of temperatures in Celsius

temperatures_celsius = [0, 10, 20, 30, 40]


# Define a lambda function that converts Celsius to Fahrenheit

convert_to_fahrenheit = lambda celsius: (celsius * 9/5) + 32


def without_lambda(celsius):

    return (celsius * 9/5) + 32

# Use the map function to apply the conversion to each temperature in the list
temperatures_fahrenheit = list(map(without_lambda, temperatures_celsius))

# Print out the list of temperatures in Fahrenheit
print(temperatures_fahrenheit)
