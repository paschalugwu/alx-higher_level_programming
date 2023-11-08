#!/usr/bin/python3
"""
We start by defining the function uniq_add with the parameter my_list
"""


def uniq_add(my_list=[]):
    """
    Use the set() function to remove duplicate elements
    from my_list and convert it into set
    """
    unique_set = set(my_list)
    """
    Next, we use the sum() function to calculate
    the sum of all elements in unique_set
    """
    sum_unique = sum(unique_set)
    """
    Finally, we return the value of sum_unique
    """
    return sum_unique
