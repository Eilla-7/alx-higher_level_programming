#!/usr/bin/python3

"""Square Class"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """square attributes
        Args:
        size: the size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
