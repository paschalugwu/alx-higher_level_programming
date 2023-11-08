#!/usr/bin/python3
"""
We start by defininh the function update_dictionary that takes in
three parameters: a_dictionary, key, and value.
"""


def update_dictionary(a_dictionary, key, value):
    """
    Inside the function, we update the dictionary by assigning the value
    to the key using the dictionary indexing
    """
    a_dictionary[key] = value
    """
    Finally, return the updatd a_dictionary from the functions
    """
    return a_dictionary
