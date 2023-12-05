#!/usr/bin/python3
"""Write a Rectangle class that inherits from BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.
    Inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes an instance.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle in the
        format "[Rectangle] <width>/<height>".
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
