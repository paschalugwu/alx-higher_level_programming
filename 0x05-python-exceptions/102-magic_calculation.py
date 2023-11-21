#!/usr/bin/python3
"""The task requires you to write a python function called
magic_calculation that performs the same operation as the
given python bytecode. The bytecode represents a loop that
iterates from 1 to 2, performs calculations based on conditions,
and handles exceptions. The goal is to replicate the behaviour
of the bytecode using Python code. We start by defining the function
magic_calculation wth the parameters a and b"""


def magic_calculation(a, b):
    # Initialize a variable result with the value 0
    result = 0
    # Use for loop to iterate 1 to 2
    for i in range(1, 3):
        # Inside the loop, use a try block to handle exceptions
        try:
            # Check if i is greater than a
            if i > a:
                """If i is greater than a, raise an exception with the
                message 'Too far' using the Exception class"""
                raise Exception('Too far')
                """If i is not greater than a, perform the
                following calculations"""
            else:
                result += a ** b / i
                # Use an except block to handle the radical exception
        except Exception:
            result = b + a
            break
    return result
