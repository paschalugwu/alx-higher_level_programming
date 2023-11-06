#!/usr/bin/python3
"""
Let's start by defining the function `max_integer`
with one parameter: `my_list`
"""


def max_integer(my_list=[]):
    """
    Inside the function, we check if the list is empty.
    If it is, we return None.
    """
    if len(my_list) == 0:
        return None
    """
    Let's initialize a variable `max_` with the first element of the list
    as the current maximum value
    """
    max_ = my_list[0]
    """
    We use a for loop to iterate through each element in the list
    """
    for x in range(0, len(my_list)):
        """
        Inside the loop, let's compare each element with the current maximum
        value. If the element is greater than the current maximum value, update
        max_ to the new maximum
        """
        if my_list[x] > max_:
            max_ = my_list[x]
            """
            After the loop, return the final maximum value
            """
    return max_
