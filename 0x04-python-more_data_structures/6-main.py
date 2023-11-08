#!/usr/bin/python3
# Let's import the module
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary
# Let's create a dictionary with the given key-value pairs
a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
"""
We now call the print_sorted_dictionary function and
pass a_dictionary as an argument
"""
print_sorted_dictionary(a_dictionary)
