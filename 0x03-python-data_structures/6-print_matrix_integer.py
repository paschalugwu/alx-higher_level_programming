#!/usr/bin/python3
"""
Let's start by defining the `print_matrix_integer`
function with one parameter: `matrix`
"""


def print_matrix_integer(matrix=[[]]):
    """
    Inside the function, let's iterate through each
    inner list (row) in the matrix
    """
    for i in matrix:
        """
        Within the outer loop, iterate through each integer
        (element) in the inner list
        """
        for j in i:
            """
            Inside the inner loop, let's print each integer using
            str.format() and end the line with a space
            """
            print("{:d}".format(j), end=" ")
            """
            After the inner loop, print a new line to move to the next row
            """
        print()
