#!/usr/bin/python3
""" definition of a class Square """


class Square:
    """
        representation of square
    """
    def __init__(self, size=0):
        """" initialize attributes

            Args:
                size: an integer of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
