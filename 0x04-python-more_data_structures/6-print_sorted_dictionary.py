#!/usr/bin/python3
"""
We start by defining the function `print_sorted_dictionary` that takes
in a single parameter, a_dictionary.
"""


def print_sorted_dictionary(a_dictionary):
    """
    Inside the function, we create a variable `sorted_keys` and
    assign it the value of the sorted keys of the dictionary
    using the sorted() function. This will sort the keys alphabetically
    """
    sorted_keys = sorted(a_dictionary)
    """
    Next, we iterate over each key in the sorted_keys list using a for loop
    """
    for key in sorted_keys:
        """
        Inside the loop, print the key-value pair using the print() function.
        Format the output string using the format() method to include the
        key and its corresponding value from dictionary
        """
        print("{:s}: {}".format(key, a_dictionary[key]))
