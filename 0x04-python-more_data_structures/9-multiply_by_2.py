#!/usr/bin/python3
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    """
        Args:
            a_dictionary: input

        Returns : double of the dictionary keys value
    """
    new_dict = dict(a_dictionary)
    for key, value in new_dict.items():
        new_dict[key] = value * 2
    return new_dict
