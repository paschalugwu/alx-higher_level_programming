#!/usr/bin/python3
"""
We start by defining the add_tuple function with two
parameters: tuple_a and tuple_b
"""


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Inside the function, let's check th length of
    tuple_a using the len() functions. If tuple_a
    has fewer than two elements, check if it has
    zero elements
    """
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
            """
            However, if tuple_a has zero elements,
            assign it the value (0, 0)
            """
        else:
            tuple_a[0], 0
    """
    Next, we handle case where tuple_b has fewer or
    more than two elements
    """
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    """
    Finally, let's return a new tuple with the first element as the addition
    of the first elements of tuple_a and tuple_b, and the second element as
    the addition of the second elements of tuple_a and tuple_b
    """
    return ((tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]))
