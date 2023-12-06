#!/usr/bin/python3
"""Function takes JSON string and returns corresponding Python code"""
import json


def from_json_string(my_str):
    """Return the Python object repesentstion of a JSON string."""
    return json.loads(my_str)
