#!/usr/bin/python3
"""Write a function that creates a Python object from JSON file."""
import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Args:
        file_name (str): The name of the JSON file.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename) as f:
        return json.load(f)
