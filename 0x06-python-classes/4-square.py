#!/usr/bin/python3
"""The task requires you to write a class called Square that
represents a square. The Square class should have a private
instance attribute called size. You need to define getter and
setter methods for the size attribute. The getter method
retrieves the value of size, while the setter method sets the
value of size with some validations. The validations include
checking if the size is integer and if it is greater than or
equal to 0. If the validations fail, appropriate exceptions
should be raised. The class should have a public instance
method called area that returns the current area of the square.
No external modules are allowed to be imported. Start by
defining the class Square"""


class Square:
    """Inside the class, define the __init__ method to initialize
    a new Square instance with a size parameter"""
    def __init__(self, size=0):
        """Inside the __init__ method, add a type check to ensure that
        size is an integer. If it is not, raise a TypeError excepption
        with the message 'size must be an integer'."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            """Add an additional check to ensure that the size is not less
            than 0. If it is, raise a ValueError exception with the message
            'size must be >= 0'."""
        elif size < 0:
            raise ValueError("size must be >= 0")
            """Finally, assign the size parameter to the private instance
            attribute __size"""
        self.__size = size
        """Define a public instance method called area that returns the
        current area of the square"""
    def area(self):
        return self.__size * self.__size
    """Define a getter method for the size attribute using the
    @property decorator"""
    @property
    def size(self):
        return self.__size
    """Define a setter method for the size attribute using the
    @size.setter decorator"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
