#!/usr/bin/python3
"""Function takes object as input and returns dictionary representation"""


def class_to_json(obj):
    """Return the dictionary representaton of a simple data structure"""
    return obj.__dict__
