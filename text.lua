py Error handiling  (Debugging is an essential skill for any Python developer)
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
