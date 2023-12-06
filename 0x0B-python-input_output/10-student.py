#!/usr/bin/python3
"""Student function that represents a student."""


class Student:
    """Represent a student."""
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the student.

        If attrs is a list of strings, represent only those attributes
        included in the list

        Args:
            attrs (list): (optional) The attributes to represent.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
