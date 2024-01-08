#!/usr/bin/python3
"""
    0-lookup
    Search available attributes and methods of an object
"""


def lookup(obj):
    """
    function that returns the list of available
    attributes and methods of an object
    """

    return dir(obj)
