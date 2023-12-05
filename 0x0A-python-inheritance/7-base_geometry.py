#!/usr/bin/python3
"""Write BaseGeometry class that inherits from BaseGeometry class"""


class BaseGeometry:
    """
    Represents a base geometry class.
    """
    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates an integer value.

        Args:
            name (str): The name of the parameter.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
