#!/usr/bin/python3
"""The task requires you to write a class called Square that
represents a square. The Square class should have a private
instance attribute called size. When instantiating the class,
you should be able to provide an optional size parameter. The
size must be an integer, otherwise, a TypeError exception should
be raised with the message 'size must be an integer'. If the size
is less than 0, a ValueError exception should be raised with
the message 'size must be >= 0'. The Square class should also
have a puublic instance method called area that returns the
current square area. You are not allowed to import any modules.
Start by defining the class"""


class Square:
    """Inside the class, define the __init__ method to initialize a new
    Square instance with a size parameter"""
    def __init__(self, size=0):
        """Inside the __init__ method, add a type check to ensure that size
        is an integer. If it is not, raise a TypeError exception with the
        message 'size must be an integer'."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            """Add an additional check to ensure that the size is not less than
            0. If it is, raise a ValueError exception with the message
            'size must be >= 0'."""
        elif size < 0:
            raise ValueError("size must be >= 0")
            """Finally, assign the size parameter to the private instance
            attribute __size"""
        self.__size = size

        """Define a public instance method called area that returns the current
        area of the square"""
    def area(self):
        return self.__size ** 2
