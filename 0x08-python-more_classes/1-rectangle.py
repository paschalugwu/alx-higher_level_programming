#!/usr/bin/python3
"""The task requires you to write a class called Rectangle that defines
a rectangle. The class should have private instance attributes width and
height. It should also have getter and setter methods for both attributes.
The getter methods should retrieve the values of the attributes, while the
setter methods should set the values of the attributes after performing
necessary checks. The class should be instantiated with optional width
and height parameters. You are not allowed to import any modules.
Start by defining the class Rectangle"""


class Rectangle:
    """Inside the clas, define the __init__ method with width and
    height as optional parameters"""
    def __init__(self, width=0, height=0):
        """Inside the __init__ method, initialize the private instance
        attributes __width and __height with the values of width and height"""
        self.__width = width
        self.__height = height
        """Define the getter method to retrieve the value of the __width"""
    @property
    def width(self):
        return self.__width
        """Define the setter method width to set the value of the __width
        attribute. Perform necessary checks to ensure that the value is an
        integer and not less than 0. Raise TypeError and ValueError exceptions
        if the checks fail"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        """Define the getter method height to retrieve the value of
        the __height attribute"""
    @property
    def height(self):
        return self.__height
    """Define the setter method height to set the value of the __height
    attribute. Perform necessary checks to ensure that the value is an
    integer and not less than 0. Raise TypeError and ValueError exceptions
    if the checks fail"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
