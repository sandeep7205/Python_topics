# Build a Polygon Area Calculator
# In this project, you will use object-oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit its methods and attributes.

# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should create a Rectangle class.

# When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

# set_width: Sets the width of the rectangle.
# set_height: Sets the height of the rectangle.
# get_area: Returns area ( width×height).
# get_perimeter: Returns perimeter ( 2(width+height) ).
# get_diagonal: Returns diagonal ( width² + height² ).
# get_picture: Returns a string that represents the shape using lines of *. The number of lines should be equal to the height and the number of * in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: Too big for picture..
# get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
# If an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10).

# You should create a Square class that subclasses Rectangle.

# When a Square object is created, it should be initialized with a single side length. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

# The Square class should contain the following methods:

# set_width: Overrides the set_width method from the Rectangle class. It should set the width and height to the side length.
# set_height: Overrides the set_height method from the Rectangle class. It should set the width and height to the side length.
# set_side: Sets the height and width of the square equal to the side length.
# The Square class should be able to access the Rectangle class methods.

# If an instance of a Square is represented as a string, it should look like: Square(side=9).

# Usage example
# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))
# That code should return:

# 50
# 26
# Rectangle(width=10, height=3)
# **********
# **********
# **********

# 81
# 5.656854249492381
# Square(side=4)
# ****
# ****
# ****
# ****

# 8
# Tests:
# Waiting:1. You should have a Rectangle class.
# Waiting:2. You should have a Square class.
# Waiting:3. The Square class should be a subclass of the Rectangle class.
# Waiting:4. The Square class should be a distinct class from the Rectangle class.
# Waiting:5. A square object should be an instance of the Square class and the Rectangle class.
# Waiting:6. The string representation of Rectangle(3, 6) should be Rectangle(width=3, height=6).
# Waiting:7. The string representation of Square(5) should be Square(side=5).
# Waiting:8. Rectangle(3, 6).get_area() should return 18.
# Waiting:9. Square(5).get_area() should return 25.
# Waiting:10. Rectangle(3, 6).get_perimeter() should return 18.
# Waiting:11. Square(5).get_perimeter() should return 20.
# Waiting:12. Rectangle(3, 6).get_diagonal() should return 6.708203932499369.
# Waiting:13. Square(5).get_diagonal() should return 7.0710678118654755.
# Waiting:14. An instance of the Rectangle class should have a different string representation after setting new values.
# Waiting:15. An instance of the Square class should have a different string representation after setting new values by using .set_side().
# Waiting:16. An instance of the Square class should have a different string representation after setting new values by using .set_width() or set_height().
# Waiting:17. The .get_picture() method should return a different string representation of a Rectangle instance.
# Waiting:18. The .get_picture() method should return a different string representation of a Square instance.
# Waiting:19. The .get_picture() method should return the string Too big for picture. if the width or height attributes are larger than 50.
# Waiting:20. Rectangle(15,10).get_amount_inside(Square(5)) should return 6.
# Waiting:21. Rectangle(4,8).get_amount_inside(Rectangle(3, 6)) should return 1.
# Waiting:22. Rectangle(2,3).get_amount_inside(Rectangle(3, 6)) should return 0.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"

        return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"


# Example Usage

rect = Rectangle(10, 5)
print(rect.get_area())

rect.set_height(3)
print(rect.get_perimeter())

print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())

sq.set_side(4)
print(sq.get_diagonal())

print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)

print(rect.get_amount_inside(sq))


"""



# ============================================================
# Polygon Area Calculator Project
# ------------------------------------------------------------
# This project demonstrates:
# 1. Object-Oriented Programming (OOP)
# 2. Classes and Objects
# 3. Inheritance
# 4. Method Overriding
# 5. Getters and Setters using @property
# 6. Encapsulation using private attributes (_width, _height)
# ============================================================


# ============================================================
# Rectangle Class
# ------------------------------------------------------------
# This is the parent/base class.
#
# A Rectangle object has:
# - width
# - height
#
# It also contains methods to:
# - calculate area
# - calculate perimeter
# - calculate diagonal
# - draw rectangle using *
# - check how many shapes fit inside
# ============================================================

class Rectangle:

    # --------------------------------------------------------
    # Constructor Method
    # --------------------------------------------------------
    # Runs automatically when object is created.
    #
    # Example:
    # rect = Rectangle(10, 5)
    #
    # width = 10
    # height = 5
    # --------------------------------------------------------
    def __init__(self, width, height):

        # Calls width setter method internally
        self.width = width

        # Calls height setter method internally
        self.height = height

    # ========================================================
    # WIDTH PROPERTY
    # ========================================================

    # --------------------------------------------------------
    # Getter Method for width
    # --------------------------------------------------------
    # Allows us to access:
    # rect.width
    #
    # Returns internal value:
    # self._width
    # --------------------------------------------------------
    @property
    def width(self):
        return self._width

    # --------------------------------------------------------
    # Setter Method for width
    # --------------------------------------------------------
    # Runs automatically when:
    # rect.width = value
    #
    # Used for:
    # - validation
    # - controlled access
    # --------------------------------------------------------
    @width.setter
    def width(self, value):

        # Validation:
        # Width cannot be negative
        if value < 0:
            raise ValueError("Width must be positive")

        # Store actual value internally
        self._width = value

    # ========================================================
    # HEIGHT PROPERTY
    # ========================================================

    # --------------------------------------------------------
    # Getter Method for height
    # --------------------------------------------------------
    @property
    def height(self):
        return self._height

    # --------------------------------------------------------
    # Setter Method for height
    # --------------------------------------------------------
    @height.setter
    def height(self, value):

        # Validation:
        # Height cannot be negative
        if value < 0:
            raise ValueError("Height must be positive")

        # Store actual value internally
        self._height = value

    # ========================================================
    # REGULAR SETTER METHODS
    # --------------------------------------------------------
    # Project specifically requires:
    # - set_width()
    # - set_height()
    #
    # These methods internally use property setters.
    # ========================================================

    # --------------------------------------------------------
    # Change width using method
    # --------------------------------------------------------
    def set_width(self, width):
        self.width = width

    # --------------------------------------------------------
    # Change height using method
    # --------------------------------------------------------
    def set_height(self, height):
        self.height = height

    # ========================================================
    # AREA METHOD
    # --------------------------------------------------------
    # Formula:
    #
    # area = width × height
    # ========================================================
    def get_area(self):
        return self.width * self.height

    # ========================================================
    # PERIMETER METHOD
    # --------------------------------------------------------
    # Formula:
    #
    # perimeter = 2(width + height)
    # ========================================================
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    # ========================================================
    # DIAGONAL METHOD
    # --------------------------------------------------------
    # Uses Pythagoras Theorem:
    #
    # diagonal = √(width² + height²)
    # ========================================================
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # ========================================================
    # PICTURE METHOD
    # --------------------------------------------------------
    # Draws rectangle using "*"
    #
    # Example:
    # width = 4
    # height = 3
    #
    # ****
    # ****
    # ****
    #
    # If width or height > 50:
    # return "Too big for picture."
    # ========================================================
    def get_picture(self):

        # Prevent huge output
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        # Empty string to build picture
        picture = ""

        # Loop through each row
        for _ in range(self.height):

            # Add stars equal to width
            picture += "*" * self.width + "\n"

        return picture

    # ========================================================
    # GET AMOUNT INSIDE METHOD
    # --------------------------------------------------------
    # Checks how many times another shape can fit inside.
    #
    # No rotation allowed.
    #
    # Example:
    # Rectangle(15,10)
    # Square(5)
    #
    # Horizontal fit:
    # 15 // 5 = 3
    #
    # Vertical fit:
    # 10 // 5 = 2
    #
    # Total:
    # 3 × 2 = 6
    # ========================================================
    def get_amount_inside(self, shape):

        # Number of shapes fitting horizontally
        horizontal_fit = self.width // shape.width

        # Number of shapes fitting vertically
        vertical_fit = self.height // shape.height

        # Total shapes fitting inside
        return horizontal_fit * vertical_fit

    # ========================================================
    # STRING REPRESENTATION METHOD
    # --------------------------------------------------------
    # Runs automatically when:
    # print(rect)
    #
    # Example Output:
    # Rectangle(width=10, height=5)
    # ========================================================
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# ============================================================
# Square Class
# ------------------------------------------------------------
# Square is a CHILD class of Rectangle.
#
# Inheritance:
# Square --> Rectangle
#
# Square inherits:
# - get_area()
# - get_perimeter()
# - get_diagonal()
# - get_picture()
# - get_amount_inside()
#
# Special Rule:
# width must ALWAYS equal height
# ============================================================

class Square(Rectangle):

    # --------------------------------------------------------
    # Constructor Method
    # --------------------------------------------------------
    # Since Square is a special Rectangle,
    # both width and height are same.
    #
    # Example:
    # Square(5)
    #
    # width = 5
    # height = 5
    # --------------------------------------------------------
    def __init__(self, side):

        # Reuse Rectangle constructor
        super().__init__(side, side)

    # ========================================================
    # OVERRIDDEN WIDTH METHOD
    # --------------------------------------------------------
    # In square:
    # changing width should ALSO change height
    # ========================================================
    def set_width(self, side):

        # Keep both dimensions equal
        self.width = side
        self.height = side

    # ========================================================
    # OVERRIDDEN HEIGHT METHOD
    # --------------------------------------------------------
    # In square:
    # changing height should ALSO change width
    # ========================================================
    def set_height(self, side):

        # Keep both dimensions equal
        self.width = side
        self.height = side

    # ========================================================
    # SET SIDE METHOD
    # --------------------------------------------------------
    # Project-specific method for square.
    #
    # Changes both width and height.
    # ========================================================
    def set_side(self, side):

        # Keep square dimensions equal
        self.width = side
        self.height = side

    # ========================================================
    # STRING REPRESENTATION
    # --------------------------------------------------------
    # Example Output:
    # Square(side=5)
    # ========================================================
    def __str__(self):
        return f"Square(side={self.width})"


# ============================================================
# EXAMPLE USAGE
# ============================================================

# Create Rectangle Object
rect = Rectangle(10, 5)

# Area = width × height = 10 × 5 = 50
print(rect.get_area())

# Change height from 5 → 3
rect.set_height(3)

# Perimeter = 2(width + height)
# = 2(10 + 3)
# = 26
print(rect.get_perimeter())

# Print rectangle object
print(rect)

# Print rectangle picture
print(rect.get_picture())


# ------------------------------------------------------------
# Create Square Object
# ------------------------------------------------------------
sq = Square(9)

# Area = 9 × 9 = 81
print(sq.get_area())

# Change side from 9 → 4
sq.set_side(4)

# Diagonal calculation
print(sq.get_diagonal())

# Print square object
print(sq)

# Print square picture
print(sq.get_picture())


# ------------------------------------------------------------
# Test get_amount_inside()
# ------------------------------------------------------------

# Rectangle becomes:
# width = 16
# height = 8
rect.set_height(8)
rect.set_width(16)

# Square side = 4
#
# Horizontal fit:
# 16 // 4 = 4
#
# Vertical fit:
# 8 // 4 = 2
#
# Total:
# 4 × 2 = 8
print(rect.get_amount_inside(sq))

"""



####################################


"""

# ==========================================================
# RECTANGLE CLASS
# ==========================================================
#
# This class is used to create Rectangle objects.
#
# Each rectangle object will have:
# - width
# - height
#
# We are using:
# - Getter methods (@property)
# - Setter methods (@width.setter, @height.setter)
#
# These help us control and validate data safely.
#
# ==========================================================

class Rectangle:

    # ------------------------------------------------------
    # Constructor Method
    # ------------------------------------------------------
    #
    # This method runs automatically when object is created.
    #
    # Example:
    # rect = Rectangle(10, 5)
    #
    # width = 10
    # height = 5
    #
    # self.width = width
    # calls the width setter automatically.
    #
    # ------------------------------------------------------

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # ======================================================
    # WIDTH GETTER
    # ======================================================
    #
    # This method runs when we access:
    #
    # rect.width
    #
    # It returns the internal value _width.
    #
    # _width is the actual variable stored in memory.
    #
    # ======================================================

    @property
    def width(self):
        return self._width

    # ======================================================
    # WIDTH SETTER
    # ======================================================
    #
    # This method runs automatically when we assign:
    #
    # rect.width = 20
    #
    # It validates width before storing value.
    #
    # ======================================================

    @width.setter
    def width(self, new_width):

        # Width cannot be negative
        if new_width < 0:
            raise ValueError("Width must be positive")

        # Store value internally
        self._width = new_width

    # ======================================================
    # HEIGHT GETTER
    # ======================================================

    @property
    def height(self):
        return self._height

    # ======================================================
    # HEIGHT SETTER
    # ======================================================

    @height.setter
    def height(self, new_height):

        # Height cannot be negative
        if new_height < 0:
            raise ValueError("Height must be positive")

        # Store value internally
        self._height = new_height

    # ======================================================
    # GET AREA
    # ======================================================
    #
    # Formula:
    #
    # area = width × height
    #
    # Example:
    #
    # width = 10
    # height = 5
    #
    # area = 50
    #
    # ======================================================

    def get_area(self):
        return self._width * self._height

    # ======================================================
    # GET PERIMETER
    # ======================================================
    #
    # Formula:
    #
    # perimeter = 2(width + height)
    #
    # ======================================================

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    # ======================================================
    # GET DIAGONAL
    # ======================================================
    #
    # Formula:
    #
    # diagonal = √(width² + height²)
    #
    # Example:
    #
    # width = 3
    # height = 4
    #
    # diagonal = √(9 + 16)
    # diagonal = √25
    # diagonal = 5
    #
    # ======================================================

    def get_diagonal(self):
        return ((self._width) ** 2 + (self._height) ** 2) ** 0.5

    # ======================================================
    # GET PICTURE
    # ======================================================
    #
    # Draws rectangle using "*" stars.
    #
    # Example:
    #
    # width = 4
    # height = 3
    #
    # Output:
    #
    # ****
    # ****
    # ****
    #
    # IMPORTANT:
    #
    # If width or height is greater than 50,
    # return:
    #
    # "Too big for picture."
    #
    # ======================================================

    def get_picture(self):

        # Prevent huge picture output
        if self._width > 50 or self._height > 50:
            return "Too big for picture."

        # Empty string to build picture
        picture = ""

        # Loop through height
        # Each loop creates one row
        for w in range(self._height):

            # Add stars and newline
            picture += "*" * self._width + "\n"

        return picture

    # ======================================================
    # GET AMOUNT INSIDE
    # ======================================================
    #
    # Calculates how many times another shape
    # can fit inside current shape.
    #
    # NO rotation allowed.
    #
    # Example:
    #
    # Rectangle(15, 10)
    # Square(5)
    #
    # width fit:
    # 15 // 5 = 3
    #
    # height fit:
    # 10 // 5 = 2
    #
    # total:
    # 3 × 2 = 6
    #
    # // means floor division
    #
    # ======================================================

    def get_amount_inside(self, other_shape):

        return (
            (self._width // other_shape.width)
            *
            (self._height // other_shape.height)
        )

    # ======================================================
    # STRING REPRESENTATION
    # ======================================================
    #
    # This method controls what prints when object
    # is printed.
    #
    # Example:
    #
    # rect = Rectangle(5, 10)
    # print(rect)
    #
    # Output:
    #
    # Rectangle(width=5, height=10)
    #
    # ======================================================

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# ==========================================================
# SQUARE CLASS
# ==========================================================
#
# Square class inherits from Rectangle class.
#
# Inheritance:
#
# Square ---> Rectangle
#
# This means Square automatically gets:
#
# - get_area()
# - get_perimeter()
# - get_diagonal()
# - get_picture()
# - get_amount_inside()
#
# A square always has:
#
# width == height
#
# ==========================================================

class Square(Rectangle):

    # ------------------------------------------------------
    # Constructor
    # ------------------------------------------------------
    #
    # A square only needs ONE side length.
    #
    # Example:
    #
    # sq = Square(5)
    #
    # width = 5
    # height = 5
    #
    # ------------------------------------------------------

    def __init__(self, side_length):

        # width and height are same in square
        self.width = side_length
        self.height = side_length

    # ======================================================
    # WIDTH GETTER
    # ======================================================

    @property
    def width(self):
        return self._width

    # ======================================================
    # WIDTH SETTER
    # ======================================================
    #
    # When width changes,
    # height should also change.
    #
    # Because:
    #
    # width == height in square
    #
    # ======================================================

    @width.setter
    def width(self, new_length):

        if new_length < 0:
            raise ValueError("Length must be positive")

        # Update both width and height
        self._width = new_length
        self._height = new_length

    # ======================================================
    # HEIGHT GETTER
    # ======================================================

    @property
    def height(self):
        return self._height

    # ======================================================
    # HEIGHT SETTER
    # ======================================================
    #
    # When height changes,
    # width should also change.
    #
    # ======================================================

    @height.setter
    def height(self, new_length):

        if new_length < 0:
            raise ValueError("Length must be positive")

        # Update both height and width
        self._height = new_length
        self._width = new_length

    # ======================================================
    # SIDE LENGTH GETTER
    # ======================================================
    #
    # side_length returns width
    # because width == height in square.
    #
    # ======================================================

    @property
    def side_length(self):
        return self._width

    # ======================================================
    # SIDE LENGTH SETTER
    # ======================================================
    #
    # When side changes,
    # both width and height must change.
    #
    # ======================================================

    @side_length.setter
    def side_length(self, new_side):

        if new_side < 0:
            raise ValueError("Side must be positive")

        # Update both dimensions
        self._height = new_side
        self._width = new_side

    # ======================================================
    # STRING REPRESENTATION
    # ======================================================
    #
    # Example:
    #
    # sq = Square(4)
    # print(sq)
    #
    # Output:
    #
    # Square(side=4)
    #
    # ======================================================

    def __str__(self):
        return f"Square(side={self.width})"


# ==========================================================
# EXAMPLE USAGE
# ==========================================================

# Create Rectangle object
rect = Rectangle(10, 5)

# Area = width × height
print(rect.get_area())

# Change height using setter
rect.height = 3

# Print perimeter
print(rect.get_perimeter())

# Print rectangle object
print(rect)

# Print rectangle shape
print(rect.get_picture())

# Create Square object
sq = Square(9)

# Print square area
print(sq.get_area())

# Change side length
sq.side_length = 4

# Print diagonal
print(sq.get_diagonal())

# Print square object
print(sq)

# Print square shape
print(sq.get_picture())

# Change rectangle dimensions
rect.height = 8
rect.width = 16

# Print how many squares fit inside rectangle
print(rect.get_amount_inside(sq))

"""