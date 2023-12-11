#!/usr/bin/python3
"""Module for Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Representation of Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return (slef.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return (self.__y)

    @y.setter
    def y(self, value):
        self.__y = value
