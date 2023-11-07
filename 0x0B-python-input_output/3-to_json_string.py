#!/usr/bin/python3
""" Defines to_json_string function """
import json

def to_json_string(my_obj):
    """
        my_obj: input to be converted
    """
    return json.dumps(my_obj)
