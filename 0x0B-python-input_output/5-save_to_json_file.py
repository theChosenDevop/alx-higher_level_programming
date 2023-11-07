#!/usr/bin/python3
"""" defines save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    """
        save_to_json_file: writes an Object to a text file,
        using a JSON representation:

        Args:
            my_obj: object to be used
            filename: receiver of the input
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
