Error handiling  (Debugging is an essential skill for any Python developer)
----
- Common error messages in python
-------------------------------------------------
   - Common Python errors include:
      - SyntaxError - if the code doesn't follow proper syntax rules.
      - NameError - if it can't find a variable by that name.
      - TypeError - when you try to perform an operation on incompatible data types.
      - IndexError - when you go out of bounds to access an index that doesn't exist in the list.
      - AtributeError - when you try to use a method or property that doesn't exist for that data type.

- Some Good Debugging Techniques in Python
-------------------------------------------------
   - Debugging is the process of identifying and resolving errors or bugs in your code. It involves examining the code, understanding the flow, and using tools to pinpoint the source of problems.
   
   - Common debugging techniques
      - Using the print function and f-strings
         - print(f'Adding {a} and {b} gives {result}')

      - Interactive Debugging with Python's built-in `pdb` Module
              ` import pdb

                def divide(a, b):
                    pdb.set_trace()
                    return a / b

                print(divide(10, 2)) ```
        - by running the cabove ode you will get  (Pdb) prompt, the write `help` and hit enter

    - IDE Debugging Tools
        - Many Integrated Development Environments (IDEs) offer advanced debugging tools, such as breakpoints, step execution, and variable inspection.
        
        - Using VS Code Debugger
            - you can set breakpoints in your code and run the debugger to pause execution at those points. Here's how to debug the same divide function:
            
            - Step 1: Set up your code Create a file called main.py with the following content:
                ``` def divide(a, b):
                        result = a / b
                        return result

                    print(divide(10, 2))
                    print(divide(15, 3))```
            - Step 2: Set a breakpoint
                - Click in the gutter (left margin) next to line 2 (result = a / b) to set a breakpoint
                - A red dot will appear, indicating the breakpoint is set
            - Step 3: Start debugging
                - Press F5 or go to Run > Start Debugging
                - Select "Python File" when prompted
                - The debugger will pause execution at your breakpoint
            - Step 4: Inspect variables
                - Hover over variables to see their current values
                - Use the Variables panel on the left to see all local variables
                - Use the Debug Console at the bottom to evaluate expressions
            - Step 5: Step through code
                - Use the debug toolbar to:
                    - Continue (F5): Resume execution until the next breakpoint
                    - Step Over (F10): Execute the current line and move to the next
                    - Step Into (F11): Enter into function calls
                    - Step Out (Shift+F11): Exit the current function

- How Does Exception Handling Work
-------------------------------------------------
   - Exception handling is the process of catching and managing errors that occur during the execution of a program, so your code doesn't crash unexpectedly. 
   - Python provides the try, except, else, and finally blocks to gracefully handle errors. 
            try:
                x = 10 / 2
            except ZeroDivisionError:
                print("You can't divide by zero!")
            except ZeroDivisionError as e: 
                # aliased to another name, Using e lets you access the actual error message or object for logging or debugging.
                print(f'Error occurred: {e}') 
            except (ValueError, ZeroDivisionError) as e:  
                # multiple exceptions in a single except clause by specifying the exceptions as a tuple
                print(f'Error occurred: {e}')
            else:
                print('Division successful:', x)
            finally:
                print('This block always runs.')

        - try: The block of code where you anticipate an error might occur.
        - except: This block runs if an error of the specified type is raised inside the try. You can also catch multiple exceptions with separate except blocks
        - else: Runs if no exception is raised in the try block.
        - finally: Runs no matter what—whether or not an exception occurred. Useful for clean-up tasks like closing files or releasing resources.

What Is the Raise Statement and How Does It Work?
-------------------------------------------------
- The raise statement is used to explicitly throw an exception at any point in your program, allowing you to signal that an error condition has occurred or that certain requirements haven't been met.
            def check_age(age):
                if age < 0:
                    raise ValueError('Age cannot be negative')
                return age

            try:
                check_age(-5)
            except ValueError as e:
                print(f'Error: {e}') # Error: Age cannot be negative

- The raise statement can also be used to re-raise the current exception, which is particularly useful in exception handling. This allows you to log or perform cleanup while still propagating the error up the call stack.
            def process_data(data):
                try:
                    result = int(data)
                    return result * 2
                except ValueError:
                    print('Logging: Invalid data received')
                    raise  # Re-raises the same ValueError

            try:
                process_data('abc')
            except ValueError:
                print('Handled at higher level')
- You can create and raise custom exceptions by defining your own exception classes with custom logic
- The raise statement can also be used with the `from` keyword to chain exceptions, showing the relationship between different errors
- You can also raise exceptions conditionally using `assert` statements, which are essentially shorthand for raise with AssertionError



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Class and object
-----------------------------------------------------------
How Do Classes Work and How Do They Differ From Objects?
-----------------------------------------------------------
- We build a `class` to `define shared behavior`, then create `objects` that `use those behaviors` or a `class` is like a `blueprint or template` you `use` to `create objects` with.

- we use the class keyword followed by the name of the class and a colon. Then within the class, you can add an initializer, along with any attributes and methods. Attributes are like variables within a class, and are used to store data. Methods are functions defined within a class, and are the actions objects created with a class can perform.
            class ClassName:
                def __init__(self, name, age):
                    self.name = name
                    self.age = age

                def sample_method(self):               
                    print(self.name.upper())
    - class ClassName is made up of the class keyword to create a class, followed by the name of the class, here called ClassName. It is common in Python to use the PascalCase convention when naming classes.
    - def __init__(self, name, age) is the special method automatically called when a new object is created. It initializes the attributes of the objects that will be created with the class.\
    - In addition to that, the first parameter of __init__ is always a reference to the specific object being created or used. By convention, this parameter is named self, but technically, you can use any name. self lets you access the object's own attributes and methods.
    - self.name = name and self.age = age are the attributes the objects will have.
    - def sample_method(self): is the method each object created can call.
    - print(self.name.upper()) is what the sample_method method will do, in this case, it prints the name in uppercase.

- You can create an object. Here's the basic syntax for creating objects from a class:
            object_1 = ClassName(attribute_1, attribute_2)
            object_2 = ClassName(attribute_1, attribute_2)

- You can also call any of the methods defined in the class from each object:
            object_1.method_name()
            object_2.method_name()

- Example - A class defines what data and behavior the object should have, and an object holds the actual data and uses that behavior. You write a class once, and you can make many objects from it, each with different data.
                class Dog:
                    def __init__(self, name, age):
                        self.name = name
                        self.age = age

                    def bark(self):
                        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

                dog_1 = Dog("Jack", 3)
                dog_2 = Dog("Thatcher", 5)

                # Call the bark method
                dog_1.bark()  # JACK says woof woof! I'm 3 years old!
                dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!

                print(dog_1.name) # Jack
                print(dog_2.age) # 5



-----------------------------------------------------------
What Are Methods and Attributes, and How Do They Work?
-----------------------------------------------------------

- Attributes are variables that belong to an object, so they hold data. There are two kinds of attributes: 
    - instance attributes
        - Instance attributes are unique to each object created from a class, and you usually set them with the __init__ method
    - class attributes.
        -  Class attributes, on the other hand, belong to the class itself and are shared by all instances of that class.

- Note:  We can access class attributes directly from the class itself, but you need to create an object and pass it data first before you can access instance attributes.

                class Dog:
                    # Class attribute (shared by all instances)
                    species = "canine" 

                    def __init__(self, name, age):
                        # Instance attributes (unique to each instance)
                        self.name = name
                        self.age = age
                    
                    def bark(self):
                        return f"{self.name} says woof woof!"

                # Create instances
                d = Dog('Fido', 5)
                e = Dog('Buddy', 3)

                # Access instance attributes (unique to each)
                print(f"{d.name} is {d.age} years old.") # Output: Fido is 5 years old.
                print(f"{e.name} is {e.age} years old.") # Output: Buddy is 3 years old.

                print(d.bark()) # Fido says woof woof!
                print(e.bark()) # Buddy says woof woof!

                # Access class attribute (shared)
                print(d.species) # Output: canine
                print(e.species) # Output: canine
                print(Dog.species) # Output: canine

                # Modify class attribute via the class (affects all)
                Dog.species = "domestic canine"
                print(d.species) # Output: domestic canine
                print(e.species) # Output: domestic canine


- Methods are functions defined inside a class. With them, any object defined from a class can perform actions that operate on or modify its own data. You also access a method with dot notation.


-----------------------------------------------------------
What Are Special Methods and What Are They Used For?
-----------------------------------------------------------
- Special methods in Python, also known as "magic methods" or "dunder methods", are special Python methods that start and end with double underscores (__). The word "dunder" itself comes from double underscores (d for double, under for underscores).
        - Example: 
        - 3 + 4 -> Python quietly runs 3.__add__(4) under the hood.
        
- Think of special methods as the directors of the activities between a person programming and the Python language interpreter itself.
        
- Python automatically calls them when certain actions happen. These operations include:
        
    - Arithmetic operations like addition, subtraction, multiplication, division, and others. In addition, __add__() is called, __sub__() for subtraction, __mul__() for multiplication, and __truediv__() for division.
        
    - String operations like concatenation, repetition, formatting, and conversion to text. __add__() is called for concatenation, __mul__() for repetition, __format__() for formatting, __str__() and __repr__() for text conversion, and so on.
        
    - Comparison operations like equality, less-than, greater-than, and others. __eq__() is called for equality checks, __lt__() for less-than, __gt__() for greater-than, and so on.
        
    - Iteration operations like making an object iterable and advancing through items. __iter__() is called to return an iterator and  __next__() to fetch the next item.
        
- When you create your own class, Python won't know how to handle things automatically. This is where special methods come in — they let you customize Python's built-in behavior.
        - Example: shopping cart where you do the following:
                - Add items to the cart
                - Remove items from the cart
                - Get the number of items in the cart
                - Check what items are in the cart
                - Check if a specific item is in the cart
                - Return or display an item at a specific index in the cart

            class Cart:
                def __init__(self):
                    self.items = []

                def add(self, item):
                    self.items.append(item)

                def remove(self, item):
                    if item in self.items:
                        self.items.remove(item)
                    else:
                        print(f'{item} is not in cart')

                def list_items(self):
                    return self.items

                def __len__(self):
                    return len(self.items)

                def __getitem__(self, index):
                    return self.items[index]

                def __contains__(self, item):
                    return item in self.items

                def __iter__(self):
                    return iter(self.items)

            cart = Cart()
            cart.add('Laptop')
            cart.add('Wireless mouse')
            cart.add('Ergo keyboard')
            cart.add('Monitor')

            for item in cart:
            print(item, end=' ') # Laptop Wireless mouse Ergo keyboard Monitor

            print(len(cart)) # 4
            print(cart[3]) # Monitor

            print('Monitor' in cart) # True
            print('banana' in cart) # False

            cart.remove('Ergo keyboard')

            print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

            cart.remove('banana') # banana is not in cart