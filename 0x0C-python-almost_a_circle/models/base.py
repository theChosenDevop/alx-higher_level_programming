#!/usr/bin/python3
""" Defines the base class for all derived class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Args:
                list_dictionaries: list of dictionaries
            Return:
                '[]' if list_dictionaries is None or empty
                or JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON representation of list_objs to a file
            Args:
                list_objs: list of objects
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
            Args:
                json_string: a string representation of a list
                            dictionaries
            Returns:
                    The list of the JSON string representation
                    json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Args:
                cls: class
                dictionary: key-value pairs
        """
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance_of_class = cls(1, 1)
            else:
                instance_of_class = cls(1)
            instance_of_class.update(**dictionary)
            return instance_of_class

    @classmethod
    def load_from_file(cls):
        """ returns a list of instance """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                dict_list = Base.from_json_string(jsonfile.read())
            return [cls.create(**item) for item in dict_list]
        except IOError:
            return []
