#!/usr/bin/python3

"""Square class"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Square definition
        Args:
        size: yhe size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return (self.__size * self.__size)
