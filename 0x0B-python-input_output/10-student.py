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

    def to_json(self, attrs=None):
        """ returns a dictionary representation of object """
        if attrs is None:
            return self.__dict__

        json_data = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_data[attr] = getattr(self, attr)
        return json_data
