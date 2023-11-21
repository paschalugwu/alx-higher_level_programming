#!/usr/bin/python3
"""The task requires you to write a function called safe_function that
executes another function safely. The safe_function takes a function fct
and any other number of arguments args. It executes the fct with the given
args and returns the result of the function. However, if an exception
occurs during the execution of the function, it returns None and prints the
error message to stderr, preceeded by "Exception:". You need to use try
and except blocks to handle exceptions. Start by importing sys module"""
import sys


# Define the function safe_function with the fct and *args parameters
def safe_function(fct, *args):
    """Inside the function, use a try block to attempt to execute the
    fct with the given args"""
    try:
        return fct(*args)
        """If an exception occurs during the execution of the fct, catch the
        exception using an except block"""
    except Exception as e:
        """Inside the except block, print the error message to stderr using
        print() and sys.exc_info()[1] to get the error message"""
        print("Exception: {}".format(e), file=sys.stderr)
        """Return None to indicate that an exception occurred during
        the execution of the fct"""
        return None
