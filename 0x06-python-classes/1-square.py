#!/usr/bin/python3
"""The task requires you to write a class called Square that defines
a square. The Square class should have a private instance attribute
called size. The class should be instantiated with a size parameter,
and there is no need to perform any type or value varification on
the size parameter. You are not allowed to import any modules.
Start by defining the class Square"""


class Square:
    """Inside the class, define the __init__ method to initialize a
    new Square instance with a size parameter"""
    def __init__(self, size):
        """Inside the __init__ method, assign the size parameter to
        the private instance attribute __size"""
        self.__size = size
