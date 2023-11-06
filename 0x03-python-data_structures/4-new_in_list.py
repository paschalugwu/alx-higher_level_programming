#!/usr/bin/python3
"""
Let's start by defining the function new_in_list with
three parameters: my_list, idx, and element
"""


def new_in_list(my_list, idx, element):
    """
    Inside the function, we create a new list called new_list and
    assign it a copy of the original list using the copy() method
    """
    new_list = my_list.copy()
    """
    Let's check if the given index is negative or greater than the
    length of the of the list minus 1. If either condition is true,
    return new_list without making modifications
    """
    if idx < 0 or idx > len(my_list) - 1:
        return new_list
        """
        If the index is within the range of the list, replace the
        element at that index with the new element in new_list
        """
    else:
        new_list[idx] = element
    """
    Finally, we return `new_list`
    """
    return new_list
