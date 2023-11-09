#!/usr/bin/python3
""" Defines the base class for all derived class """


class Base:
    """  superclass Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            initialize the instance of a class

            self: object representation
            id: id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
