#!/usr/bin/python3
"""
Let's start by defining the function no_c
with one parameter: `my_string`
"""


def no_c(my_string):
    """
    Let's create a dictionary called `my_dic` that
    maps the Unicode values of the of the characters
    'c' and 'C' to None. This dictionary will be
    used for translation later
    """
    my_dict = {ord('c'): None, ord('C'): None}
    """
    We now use the translate() method of the string to remove
    the characters'c' and 'C' based on the translation dictionary
    """
    return my_string.translate(my_dict)
