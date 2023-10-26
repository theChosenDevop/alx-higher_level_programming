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
        self.size = size

    def area(self):
        """ Returns: the current square area """
        return self.__size * self.__size

    @property
    def size(self):
        """ Returns the size of square class """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ prints in stdout the square """
        for element in range(self.__size):
            [print("#", end="") for i in range(0, self.__size)]
            print()
        elif self.__size == 0:
            print()
