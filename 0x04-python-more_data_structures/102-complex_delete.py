#!/usr/bin/python3
"""
Start by defining the function  complex_delete  that
takes in two parameters:  a_dictionary  and  value .
"""


def complex_delete(a_dictionary, value):
    """
    Inside the function, create a list  list_keys
    that contains all the keys of the  a_dictionary
    """
    list_keys = list(a_dictionary.keys())
    """
    Iterate over each key  value_dic  in  list_keys
    """
    for value_dic in list_keys:
        """
        Inside the loop, check if the value associated with the current
        key ( a_dictionary.get(value_dic) ) is equal to the specified value
        """
        if value == a_dictionary.get(value_dic):
            """
            If the value matches, delete the key-value pair from the
            a_dictionary  using the  del  keyword
            """
            del a_dictionary[value_dic]
            """
            After the loop, return the modified  a_dictionary
            """
    return a_dictionary
