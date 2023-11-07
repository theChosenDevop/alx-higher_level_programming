#!/usr/bin/python3
""" defines a class Student """


class Student:
    """"A class student"""

    def __init__(self, first_name, last_name, age):
        """
            first_name: user first name
            last_name: user last name
            age: user age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns a dictionary representation of object """
        return self.__dict__
