#!/usr/bin/python3
"""Module of 'look up' method"""


def lookup(obj):
    """lookup object attributes & methods
    Args:
        obj (object): the object list

    Returns:
        list: list of attributes
    """
    return (dir(obj))
