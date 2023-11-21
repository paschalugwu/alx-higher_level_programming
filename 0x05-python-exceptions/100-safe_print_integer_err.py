#!/usr/bin/python3
"""The task requires you to write a function called safe_print_integer_err
that prints an integer value. The function should handle different types of
input values, such as integers or strings, and print the integer value
followed by a new line. It should return True if the value is an integer and
has been printed correctly. If the value is not an integer, it should return
False and print an error message to stderr, preceded by "Exception:". You
need to use try and except blocks to handle exceptions, and use "{:d}.format()
to print the integer value. You are not allowed to use the type() function.
Let's start by importing the sys module. We import the sys module in order to
access the sys.exc_info() function, which provides information about the
current exception being handled. In this case, we use sys.exc_info()[1]
to retrieve the error message associated with the exception and include it
in the error message printed to stderr"""
import sys


# Define the function safe_print_integer_err with the value parameter
def safe_print_integer_err(value):
    """Inside the function, use a try block to attempt to print the value as
    an integer using "{:d}".format()"""
    try:
        print("{:d}".format(value))
        """If the value is an integer and has been printed correctly,
        return True"""
        return True
        """If an exception (TypeError or ValueError) occcurs during the
        execution of the try block, catch the exception
        using an except block"""
    except (TypeError, ValueError):
        """Inside the except block, print the error message to stderr using
        print() and sys.exc_info()[1] to get the error message"""
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        """Return False to indicate that the value is not an integer and has
        not been printed correctly"""
        return False
