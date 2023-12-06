#!/usr/bin/python3
"""Create Pascal triangle function"""


def pascal_triangle(n):
    """
    Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.

    Args:
        n (int): The size of the Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
