'''
Build a Number Pattern Generator
In this lab you will practice the basics of Python by building a small app that creates a number pattern.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should define a function named number_pattern that takes a single parameter n (representing a positive integer).
number_pattern should use a for loop.
number_pattern(n) should return a string with all the integers starting from 1 up to n (included) separated by a space. For example, number_pattern(4) should return the string 1 2 3 4.
If the argument passed to the function is not an integer value, the function should return Argument must be an integer value..
If the argument passed to the function is less than 1, the function should return Argument must be an integer greater than 0..

'''

def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    str_list = " ".join([str(i) for i in range(1, (n+1))])
    return str_list
print(number_pattern(5))