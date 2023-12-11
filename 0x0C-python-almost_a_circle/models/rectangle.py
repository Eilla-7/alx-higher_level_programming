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
        return (self.__x)

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

    def display(self):
        """Prints the rectangle with # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

    def __str__(self):
        """Returns string information"""
        return (
                '[{}] ({}) {}/{} - {}/{}'
                .format(
                    type(self).__name__,
                    self.id,
                    self.x,
                    self.y,
                    self.width,
                    self.height
                    )
        )

    def updatee(self, id=None, width=None, height=None, x=None, y=None):
        """Assigns an argument to each attribute"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""
        if args:
            self.updatee(*args)
        elif kwargs:
            self.updatee(**kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
