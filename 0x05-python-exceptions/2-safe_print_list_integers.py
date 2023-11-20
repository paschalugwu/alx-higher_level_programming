#!/usr/bin/python3
"""The task requires you to write a function called
safe_print_list_integers that takes a list and  number x as
input and prints the first x elements of the list that are
integers. The function should skip any non-integer values in
the list and only print the integers on the same line followed
by a new line. The function should return the real numbers of
the integers printed. You are not allowed to import any modules
or use the len() function. We start by defining the function
safe_print_list_integers with the my_list and x parameters"""


def safe_print_list_integers(my_list=[], x=0):
    """Initialize a variable count to keep track of the number
    of integers printed"""
    count = 0
    # Use a for loop to iterate over the first x elements of the list
    for i in range(x):
        """Inside the loop, use a try block to attempt to print the
        current element as integer using "{:d}".format(). If the
        current element is an integer, increment by the count varable"""
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
            """If an exception is raised durng the execution of the try
            block, it means the current element is not an integer. Catch
            the exception using an except block, and skip to the next
            element"""
        except (ValueError, TypeError):
            continue
            """After the loop, print a new line to seperate the integers
            from any other output"""
    print("")
    """Return the count variable, which represents the number of
    integers printed"""
    return count
