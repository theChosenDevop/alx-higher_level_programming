#!/usr/bin/python3
""" Defines load_from_json_file """
import json


def load_from_json_file(filename):
    """
        load_from_json_file: creates an Object from a “JSON file”

        Args:
            filename: file to be use
    """
    with open(filename) as f:
        return json.load(f)
