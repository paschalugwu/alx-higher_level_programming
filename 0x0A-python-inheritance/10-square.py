#!/usr/bin/python3
"""class Square that inherits from the Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init(self, size): Initializes a Square instance.
        area(self): Calculates the area pf the square.
    """
    def __init__(self, size):
        """
        Initializes a square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        REturns:
            int: The area of teh square.
        """
        return self.__size ** 2
