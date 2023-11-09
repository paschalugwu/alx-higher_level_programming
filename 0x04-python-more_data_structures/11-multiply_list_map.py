#!/usr/bin/python3
"""
Let's start by defining the function multiply_list_map that
takes in two parameters: my_list (with a default value of an
empty list) and number (with a default value of 0)
"""


def multiply_list_map(my_list=[], number=0):
    """
    Inside the function, we use the map function to apply a lambda
    function to each element of my_list. The lambda function
    multiplies each element by the given number
    """
    return (list(map((lambda i: i * number), my_list)))
