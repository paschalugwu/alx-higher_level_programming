#!/usr/bin/python3
"""
Let's start by defining the function common_elements
with the parameters set_1 and set_2.
"""


def common_elements(set_1, set_2):
    """
    Let's now use a comprehension to iterate over each element
    in set_2 and check if it is also present in set_1
    """
    common_set = {x for x in set_2 if x in set_1}
    """
    Finally, we return the common_set as the result
    """
    return common_set
