#!/usr/bin/python3
"""
We start by defining the add_tuple function with two
parameters: tuple_a and tuple_b
"""


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Let's create an empty tuple called `new_tuple` to store the result
    """
    new_tuple = ()
    """
    We're going to extend tuple_a with two additional elements,
    each having the value 0. If a tuple has fewer than
    two elements, the missing elements are assumed to be
    0. This is handled by using the value 0 for each missing
    integer when performing addition. If the tuple has more than
    two elements, only the first two elements are considered
    for addition. This ensures that the resulting tuple always has
    exactly two elements.
    """
    tuple_1 = tuple_a + (0, 0)
    """
    Let's extend tuple_b with two additional elements
    each having the value 0. We do this for the same reason why
    we extended tuple_a above.
    """
    tuple_2 = tuple_b + (0, 0)
    """
    Let's calculate the first element of the new_tuple by adding the first
    elements of tuple_1 and tuple_2, and calculate the secoond element by
    adding the second element elements of tuple_1 and tuple_2
    """
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    """
    Finally, we return the `new_tuple`
    """
    return new_tuple
