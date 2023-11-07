#!/usr/bin/python3
""" defines class_to_json function  """
import json


def class_to_json(obj):
    """
        class_to_json: returns the dictionary description with simple data
                        structure (list, dictionarystring, integer and boolean)
                        for JSON serialization of an object

        obj: instance of a class
    """
    return obj.__dict__
