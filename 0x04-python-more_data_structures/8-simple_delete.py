#!/usr/bin/python3
"""
We start by defining the function simple_delete that
takes two parameter: a_dictionary and key.
"""


def simple_delete(a_dictionary, key=""):
    """
    Inside the function, we use an if statement to check if th key exists
    in the a_dictioary. We use the `in` keyword to check for existence
    """
    if key in a_dictionary:
        """
        If the key exists in the dictionary, we use the del keyword to delete
        the key-value par from the dictionar
        """
        del a_dictionary[key]
        """
        Finally, we return th updated a_dictionary from th funtion
        """
    return a_dictionary
