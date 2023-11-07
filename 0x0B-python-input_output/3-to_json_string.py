#!/usr/bin/python3
import json
""" Defines t0=o_json_string function """


def to_json_string(my_obj):
    """
        my_obj: input to be converted
    """
    return json.dumps(my_obj)
