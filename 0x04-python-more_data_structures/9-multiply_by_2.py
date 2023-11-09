#!/usr/bin/python3
"""
We start by defining the function multiply_by_2 that takes
in a single parameter, a_dictionary.
"""


def multiply_by_2(a_dictionary):
    """
    Inside the function, we use a dictionary comprehension
    to create a new dictionary with the same keys as
    a_dictionary, but with values multiplied by 2. We would
    iterate over the key-value pairs of a_dictionary using
    the items() method
    """
    return {k: v * 2 for k, v in a_dictionary.items()}
