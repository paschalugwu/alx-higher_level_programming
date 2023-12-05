#!/usr/bin/python3
"""Write a MyInt class that inherits from the int class"""


class MyInt(int):
    """
    A class that represents an integer with inverted == and != operators."
    """
    def __eq__(self, value):
        """Overide the == operator with the != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overide the != operator with == behavior."""
        return self.real == value
