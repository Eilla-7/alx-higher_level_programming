#!/usr/bin/python3
"""Module for Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String info"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
