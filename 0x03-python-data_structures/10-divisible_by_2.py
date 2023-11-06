#!/usr/bin/python3
"""
Let's start by defining the function `divisible_by_2`
with one parameter: my_list
"""


def divisible_by_2(my_list=[]):
    """
    Inside the function, we use map() function to apply
    a lambda function to each element of the list.
    This are the activities that take place:
    1. The lambda function checks if each element x in the list is
    divisible by 2. If it is, it returns True; otherwise, it returns false.
    2. The map() function applies the lambda function to each element of
    the list and returms a map object. To convert the map object into a list,
    use the list() function.
    3. Finally, we return the resulting list from divisible_by_2 fuction.
    """
    return list(map(lambda x: True if x % 2 == 0 else False, my_list))
