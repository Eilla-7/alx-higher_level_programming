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
        self.int_validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        self.int_validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return (slef.__x)

    @x.setter
    def x(self, value):
        self.int_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return (self.__y)

    @y.setter
    def y(self, value):
        self.int_validation("y", value)
        self.__y = value

    def int_validation(self, name, value, equal=True):
        """Function to valisate attributes"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if equal and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not equal and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Returns the area of the recktangle"""
        return (self.width * self.height)
