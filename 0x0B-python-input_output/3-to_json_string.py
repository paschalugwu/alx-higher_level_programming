#!/usr/bin/python3
"""Write a `to_json_string` that takes an object as input
and returns its JSON representation as a string"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.
    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
