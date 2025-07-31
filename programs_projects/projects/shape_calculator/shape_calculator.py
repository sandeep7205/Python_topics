import math
import sys

# ✅ Validate numeric input and ensure it's a positive number
def input_number_validation(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("❌ Please enter a positive number.")
        except ValueError:
            print("❌ Invalid input. Enter a number.")

# ✅ Ask user if they want to continue; return True or False
def ask_to_continue():
    while True:
        again = input("\n🔁 Do you want to try a new shape calculation? (y/n): ").strip().lower()
        if again in ['y', 'yes']:
            return True
        elif again in ['n', 'no', 'exit']:
            return False
        else:
            print("❌ Invalid input. Please type 'y' or 'n'.")

# 🟢 Calculate area of a circle
def circle_area(unit):
    radius = input_number_validation("Enter the radius: ")
    area = round(math.pi * radius ** 2, 2)
    print(f"\n✅ Area of Circle: {area} {unit}²\n")

# 🟢 Calculate area of a square
def square_area(unit):
    side = input_number_validation("Enter the side: ")
    area = round(side ** 2, 2)
    print(f"\n✅ Area of Square: {area} {unit}²\n")

# 🟢 Calculate area of a triangle
def triangle_area(unit):
    base = input_number_validation("Enter the base: ")
    height = input_number_validation("Enter the height: ")
    area = round(0.5 * base * height, 2)
    print(f"\n✅ Area of Triangle: {area} {unit}²\n")

# 🟢 Calculate area of a rectangle
def rectangle_area(unit):
    length = input_number_validation("Enter the length: ")
    width = input_number_validation("Enter the width: ")
    area = round(length * width, 2)
    print(f"\n✅ Area of Rectangle: {area} {unit}²\n")

# 🔴 Exit the program gracefully
def exit_program(_=None):  # Optional param to match function signatures
    print("👋 Exiting the Shape Calculator. Thank you!")
    sys.exit()

# 📌 Shape name to function mapping
shape_functions = {
    "circle": circle_area,
    "square": square_area,
    "triangle": triangle_area,
    "rectangle": rectangle_area,
    "exit": exit_program
}

# 📌 List of allowed units
allowed_units = ["cm", "m", "in", "mm", "ft"]

# 🎉 Program starts here
print("\n🎉 Welcome to the Shape Area Calculator!\n")

# 🔁 Main loop to allow repeated calculations
while True:
    # 🧾 Display available shape options
    shape_list_str = '\n'.join(f"- {shape.capitalize()}" for shape in shape_functions)
    shape_input = input(f"Available shapes:\n{shape_list_str}\n\n👉 Choose a shape: ").strip().lower()

    # ❌ Keep asking if input is invalid
    while shape_input not in shape_functions:
        shape_input = input("❌ Invalid input. Please choose a valid shape: ").strip().lower()

    # 📏 Ask for unit input
    unit_input = input("Enter unit (cm/m/in/mm/ft): ").strip().lower()
    while unit_input not in allowed_units:
        unit_input = input("❌ Invalid unit. Please enter a valid unit (cm/m/in/mm/ft): ").strip().lower()

    # ✅ Call the selected shape's function
    shape_functions[shape_input](unit_input)

    # 🔁 Ask if user wants to repeat
    if not ask_to_continue():
        print("\n👋 Exiting the Shape Calculator. Thank you!")
        break
