#!/usr/bin/python3
""" Defines from_json_string function """
import json


def from_json_string(my_str):
    """
        from_json_string: returns an object(Python data structure)
                          represented by a JSON string
        my_str: user input
    """
    return json.loads(my_str)
