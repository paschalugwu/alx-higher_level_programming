#!/usr/bin/python3
"""Defines a locked class that prevents dynamic
creation of instance attribute"""


class LockedClass:
    """Prevent the user from dynamically creating new instance
    attributes, except if the new instance attribute is
    called 'first_name'."""
    __slots__ = ("first_name",)
