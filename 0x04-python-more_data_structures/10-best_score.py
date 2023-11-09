#!/usr/bin/python3
"""
We start by defining the function best_score that takes
a single parameter, a_dictionary.
"""


def best_score(a_dictionary):
    """
    Inside the function, we use an if statement to check
    if the a_dictionary is None or an empty dictionary.
    We can use the `is` operator to check for None and the
    == operator to check for an empty dictionary.
    """
    if a_dictionary is None or a_dictionary == {}:
        """
        If the dictionary is None or empty, we return None
        """
        return None
        """
        However, if the a_dictionary is not None or an empty dictionary,
        we use the max() function with the key parameter set to
        a_dictionary.get to find the key with the highest integer value
        in the dictionary
        """
    return max(a_dictionary, key=a_dictionary.get)
