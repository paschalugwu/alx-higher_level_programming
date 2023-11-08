#!/usr/bin/python3
"""
We start by defining the function search_replace with
the parameters my_list, search, and replace.
"""


def search_replace(my_list, search, replace):
    """
    Let's now create a new list called new_list
    to store the modified elements.
    """
    new_list = []
    """
    Next, we use loop to iterate over each element in my_list
    """
    for element in my_list:
        """
        Inside the loop, we check if the current element is
        equal to the search element.
        """
        if element == search:
            """
            If the condition is true, we append the
            replace element to the new_list.
            """
            new_list.append(replace)
            """
            If the condition is false, append the current element
            to new_list without modification.
            """
        else:
            new_list.append(element)
            """
            After loop finishes, we return the new_list
            """
    return new_list
