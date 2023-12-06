#!/usr/bin/python3
"""Module for is_same_class method."""


def is_same_class(obj, a_class):
    """See if an object is exactly an instance"""
    return obj.__class__ is a_class
