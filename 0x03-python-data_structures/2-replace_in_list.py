#!/usr/bin/python3
"""
Let's start by defining the function `replace_in_list`
with three parameters: my_list, idx, and element.
"""


def replace_in_list(my_list, idx, element):
    """
    Inside the function, let's check if the given index is
    negative or greater than the length of the list minus 1.
    If either conditions is true, return the original list
    without any modifications
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
        """
        If the index is within the range, replace the element
        at the index with the new element
        """
    else:
        my_list[idx] = element
    return my_list
