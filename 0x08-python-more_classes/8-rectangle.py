#!/usr/bin/python3
"""
    0-rectangle Module
    Private intsance of width and height
"""


class Rectangle:
    """ Rectangle class with object attributes width and height. """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
         Initialize instance of Rectangle
         Args:
            width: object method of the class
            height: object method of the class
         """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ dunder should print the rectangle with the character #
        """
        str_hash = ""
        if self.__height == 0 or self.__width == 0:
            return str_hash
        for index in range(self.__height):
            for index_2 in range(self.__width):
                str_hash += str(self.print_symbol)
            str_hash += '\n'
        return str_hash[:-1]

    def __repr__(self):
        """ Return a string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """" Print the message Bye rectangle... (... being 3 dots not ellipsis)
        when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Args:
                rect1: area of first object of Rectangle
                rect2: area pf second object of Rectangle
            Return:
                the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
