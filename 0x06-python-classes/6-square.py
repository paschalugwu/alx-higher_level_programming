#!/usr/bin/python3
"""The task requires you to write a class called Square that represents
a square. The Square class should have a private instance attribute
called size and position. You need to define getter and setter methods
for these attributes. The getter methods should retrieve the values of
the size and position, while the setter methods should set the values
with some validations. The class should also have public instance method
for calculating the area of the square and printing the square. The
printing method shhould use the # character to represent the square, and
the position attribute should be used to determine the position of
the square. You are not allowed to import any modules. Start by defining
the class Square"""


class Square:
    """Inside the class, define the __init__ method with size and position
    parameters."""
    def __init__(self, size=0, position=(0, 0)):
        """Inside the  __init__  method, initialize the private instance
        attributes  __size  and  __position  with the values of the
        parameters."""
        self.size = size
        self.position = position
        """Define a getter method for the size attribute using the @property
        decorator."""
    @property
    def size(self):
        """Inside the getter method, return the value of the private
        instance __size"""
        return self.__size
    """Define the setter method for the size attribute using @size.setter
    decorator"""
    @size.setter
    def size(self, value):
        """Inside the setter method, perform validations to ensure that
        the value being set is an integer and is not less thab 0. Raise
        TypeError and ValueError exceptions with appropriate error messages
        if validations fail. Otherwise, assign the value to the private
        instance attribute __size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        """Define a getter method for the position attribute using the
        @property decorator"""
    @property
    def position(self):
        """Inside the getter method, return the value of the private
        instance attribute __position."""
        return self.__position
    """Define the setter method for the position attribute using the
    @position.setter decorator."""
    @position.setter
    def position(self, value):
        """Inside the setter method, perform validations to ensure that
        the value being set is a tuple of 2 positive integers. Raise a
        TypeError exception with an appropriate error message if the
        validations fail. Otherwise, assign the value to the private
        instance attribute __position."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """Define a public instance method called area that calculates and returns
    the area of the square"""
    def area(self):
        """Inside the area method, calculate the area by multiplying the
        private instance attribute __size by itself. Return the result"""
        return self.__size * self.__size
    """Define a public instance method called my_print that prints the square
    with # character"""
    def my_print(self):
        """Inside the my_print method, check if the private instance attribute
        __size is equal to 0. If it is, print an empty line and return."""
        if self.__size == 0:
            print("")
            return
        """Use a loop to print the square with # character. Use the private
        instance attribute __position to determine the position of the square.
        If __position[1] is greater than 0, print the necessary number of empty
        lines before printing the square"""
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
