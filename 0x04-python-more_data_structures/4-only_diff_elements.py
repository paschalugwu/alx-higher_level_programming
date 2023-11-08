#!/usr/bin/python3
"""
Let's start by defining the function `only_diff_elements`
with the parameters set_1 and set_2
"""


def only_diff_elements(set_1, set_2):
    """
    Let's use the symmetric_difference() method to find the elements
    that are present in only one of the input sets.
    """
    diff_set = set_1.symmetric_difference(set_2)
    """
    Finally, we return diff_set as the result.
    """
    return diff_set
