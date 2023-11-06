#!/usr/bin/python3
"""
Let's start by defining the function `print_reversed_list_integer`
with a parameter `my_list`
"""


def print_reversed_list_integer(my_list=[]):
    """
    Inside the function, let's check if the input my_list is an
    instance of a list to ensure it is a valid input
    """
    if isinstance(my_list, list):
        """
        If the iput is a valid list, reverse the order of the
        elements in thr list using the reverse() method
        """
        my_list.reverse()
        """
        Next, we iterate through each element in the reversed
        list and print it using str.format()
        """
        for i in my_list:
            print("{:d}".format(i))
