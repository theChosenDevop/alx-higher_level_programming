#!/usr/bin/python3
# 11-multiply_list_map.py

def multiply_list_map(my_list=[], number=0):
    """

        Args:
            my_lists: list of integers
            number: integer

        Returns:
            list of integer multiplied by number
    """
    return list(map(lambda x: x * number, my_list))
