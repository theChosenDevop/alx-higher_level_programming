#!/usr/bin/python3
# 6-print_sorted_dictionary.py

def print_sorted_dictionary(a_dictionary):
    """
        Args:
            a_dictionary: dictionary argument

        Returns:
            sorted dictionary
    """
    for key in sorted(a_dictionary):
        print("{} : {}".format(key, a_dictionary[key]))
