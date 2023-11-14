#!/usr/bin/python3
""" Defines derived class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ inherits from superclass Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Args:
                 width(int): The width of Rectangle
                 height(int): The height of Rectangle
                 x(int): The x axis of the Rectangle
                 y(int): The y axis of the Rectangle
                 id(int): The id of the object
            Raises:
                TypeError: If width, height, x ,y is not an integer
                ValueError: If width or height <= 0
                ValueError: If x or y < 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """ Returns the string representation of the object"""
        return ("[Rectangle] ({}) {}/{} - {}/{}\
                ".format(self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        """ Get the width of the object"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width attribute of the object"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the object """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the object """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get the x attribute of the object """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the x attribute of the object """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get the y attribute of the object """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the y attribute of the object """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ get area of a rectangle """
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for i in range(self.y):
            print("")
        lines = [" " * self.x + '#' * self.width for _ in range(self.height)]
        print('\n'.join(lines))

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        attributes = ["id", "width", "height", "x", "y"]

        if args and len(args) != 0:
            for i in range(min(len(args), len(attributes))):
                setattr(self, attributes[i], args[i])
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
