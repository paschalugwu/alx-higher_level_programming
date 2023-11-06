#!/usr/bin/python3
"""
Let's start by defining the function `delete_at`
with two parameters: `my_list` and `idx`
"""


def delete_at(my_list=[], idx=0):
    """
    Inside the function, we check if the given index is greater than or
    equal to 0 and less than the length of the list. This ensures that the
    index is within the valid range
    """
    if idx >= 0 and idx < len(my_list):
        """
        If the index is within the valid range, use the `del` keyword to
        delete the item at the specified index
        """
        del my_list[idx]
        """
        Finally, we return the modified list
        """
    return my_list
