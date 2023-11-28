#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """Reprecentation of a Rectangle class"""
    def __init__(self, width=0, height=0):
        """initiate the Rectangle"""
        self.height = height
        self.width = width

        @property
        def width(self):
            """getter for width attribute"""
            return (self.__width)

        @width.setter
        def width(self, value):
            """setter for the width attribute"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """getter for the height attribute"""
            return (self.__height)

        @height.setter
        def height(self, value):
            """setter for height attribute"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value