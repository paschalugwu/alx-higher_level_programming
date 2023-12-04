#!/usr/bin/python3


class MyList(list):
    """
    This class represents a custom list that
    inherits from the built-in list class.
    """
    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        print(sorted(self))
        """
        Sorts the elements of the list in ascending order and prints them
        """
