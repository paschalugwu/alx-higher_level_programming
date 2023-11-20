#!/usr/bin/python3
"""Lets define the function safe_print_list that takes two
arguments: my_list and x. The default value for my_list is
an empty list, and the default value for x is 0."""


def safe_print_list(my_list=[], x=0):
    """The next line will initialize the variable ret to 0, which
    will be used to keep track of the number of elements actually printed"""
    ret = 0
    """Next, we start a for loop that iterates over the rage of x elements
    to be printed. The loop variable i takes on the vaues 1, 2,...,x-1."""
    for i in range(x):
        """The next block of code tries to print the i-th element of the
        my_list using the print() function. If the i-th element is not found,
        an IndexError exception is raised, and the loop is broken using the
        break statement. If the i-th element is found in the list, it is
        printed using the print() function, and the ret variable is
        incremented by 1."""
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
        """We are now going to print a newline character to seperate the
        output from the next line"""
    print("")
    # Finally we return ret variable (number of elements actually printed)
    return (ret)
