#!/usr/bin/python3
"""
Let's start by defining the function element_at
with two parametes: my_list and idx
"""


def element_at(my_list, idx):
    """
    Inside the function, let's check if the given index
    is negative or greater than the length of the list minus 1.
    If either condition is tru, return None
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
        """
        However, if the index is within the range of the list,
        return the element at that index
        """
    else:
        return my_list[idx]
