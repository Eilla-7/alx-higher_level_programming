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

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def updatee(self, id=None, size=None, x=None, y=None):
        """Update the data"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
    
    def update(self, *args, **kwargs):
        """Update attributes"""
        if args:
            self.updatee(*args)
        elif kwargs:
            self.updatee(**kwargs)
