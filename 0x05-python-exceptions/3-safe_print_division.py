#!/usr/bin/python3
"""The task requires you to write a function called
safe_print_division that takes two integers a and b as input.
The function should divide a by b and print the result using the
"{:}".format() method. The division shoulld be performed inside
a try block, and any exceptions (TypeError or ZeroDivisionError)
should be caught using an except block. The function should always
print the result, preceeded by "Inside result", using the finally
block. The function should return the value of the division if it
is successful, or None otherwise. You are not allowed to import
any modules. We start by defining the function safe_print_division
with the a and b parameters"""


def safe_print_division(a, b):
    """Inside the function, use a try block to perform the
    division of a by b"""
    try:
        div = a / b
        """If the division is successful, assign the result to a variable
        div. If an exception (TypeError or ZeroDivisionError) occurs
        during the division, assign None to div"""
    except (TypeError, ZeroDivisionError):
        div = None
        """Use the finally block to always print the result, preceeded
        by "Inside result", using the "{:}".format() method"""
    finally:
        print("Inside result: {}".format(div))
        # Return the value of div
    return div
