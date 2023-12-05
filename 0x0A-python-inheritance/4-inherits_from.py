#!/usr/bin/python3
"""Check if object is an instance of class"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        If obj is an inherited instance of a_class - True,
        Otherwise - False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
