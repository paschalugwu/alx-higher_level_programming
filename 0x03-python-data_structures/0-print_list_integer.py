#!/usr/bin/python3
"""
Let'd define the function `print_list_integer`
with parmeter `my_list`
"""


def print_list_integer(my_list=[]):
    """
    Now, we need to iterate through each element
    in the my_list and print it.
    """
    for i in my_list:
        """
        Inside the loop, we need to print each
        integer using `str.format()`
        """
        print("{:d}".format(i))
