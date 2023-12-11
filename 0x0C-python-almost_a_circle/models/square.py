#!/usr/bin/python3
"""Module for Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)
