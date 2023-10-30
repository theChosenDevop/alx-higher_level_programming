#!/usr/bin/python3
"""
    0-rectangle Module
    Private intsance of width and height
"""


class Rectangle:
    """ Rectangle class with object attributes width and height. """

    def __init__(self, width=0, height=0):
        """
         Initialize instance of Rectangle
         Args:
            width: object method of the class
            height: object method of the class
         """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves the width  property of class instance """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width of instance of class
            Args:
                value: value of width, must be positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves the width property of class instance """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Sets height of object of a Rectangle class
            Args:
              value: value of height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ public instance method """
    def area(self):
        """ area: product of width and height """
        return self.__width * self.__height

    def perimeter(self):
        """ perimter of rectangle class instance """
        return (self.__width + self.__height) * 2
