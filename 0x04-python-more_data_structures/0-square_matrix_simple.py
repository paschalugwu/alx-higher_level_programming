#!/usr/bin/python3
"""
Let's start by defining the function square_matrix_simple
with the parameter matrix. We set the default value of
matrix as an empty list.
"""


def square_matrix_simple(matrix=[]):
    """
    Let's now create a copy of the input matrix using the copy()
    to ensure that the initial matrix is not modified.
    """
    new_matrix = matrix.copy()
    """
    Next, we use a for loop to iterate over each row in the matrix.
    Use the range () function with len(matrix) to get the index
    of each row.
    """
    for i in range(len(matrix)):
        """
        Inside the loop, we will use the map() function to apply a lambda
        function to each element in the current row. The lambda function
        should square the element.
        """
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
        """
        After the loop finishes, we return the new_matrix.
        """
    return new_matrix
