#!/usr/bin/python3
"""The task requires you to write a function called raise_exception_msg
that raises a NameError exception with a given message. You are not
allowed to import any modules. We start by defining the function
raise_exception_msg with the message parameter"""


def raise_exception_msg(message=""):
    """Inside the function, use the raise keyword to raise a NameError
    exception with the given message"""
    raise NameError(message)
