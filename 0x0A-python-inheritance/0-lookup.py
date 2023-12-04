#!/usr/bin/python3
"""Defines a function to lookup objects attributes and methods."""


def lookup(obj):
    """Return a list of available attributes and methods of an object"""
    return dir(obj)
