#!/usr/bin/python3
"""Add all arguments to a python list and save them to a file."""


import sys


# Import the required functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    # Load the list of items from the add_item.json file
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    # If the file doesn't exist, create a newlist
    items = []

# Add command-line aruments to the list
items.extend(sys.argv[1:])

# Save the list of items to the add_items.json file
save_to_json_file(items, "add_item.json")
