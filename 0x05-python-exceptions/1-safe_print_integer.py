#!/usr/bin/python3
"""This task requires you to write a function called safe_print_integer
that takes a value as input and prints it as an integer using the
"{:d}".format method. The function should return True if the value is
an integer and has been printed correctly, and False otherwise. You
need to handle exceptions using try and except blocks, and you are not
allowed to import any modules or use the type() function. The first
approach to this task is to define the function safe_print_integer with
the value parameter"""


def safe_print_integer(value):
    """Inside the function, use a try block to attempt to print the value
    as an integer using "{:d}".format()"""
    try:
        print("{:d}".format(value))
        """If the try block executes successfully, it means the value is
        an integer and has been printed correctly. In this case, return
        True"""
        return True
        """If an exception is raised during the execution of the try block,
        it means the value is not an integer or cannot be printed as an
        integer. Catch the exception using the except block,
        and return False"""
    except (TypeError, ValueError):
        return False
