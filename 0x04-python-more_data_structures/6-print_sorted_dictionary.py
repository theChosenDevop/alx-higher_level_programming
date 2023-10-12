#!/usr/bin/python3
# 6-print_sorted_dictionary.py

def print_sorted_dictionary(a_dictionary):
    """
        Args:
            a_dictionary: dictionary argument

        Returns:
            sorted dictionary
    """
    dict_sort = sorted(a_dictionary)
    for i in dict_sort:
        print("{}: {}".format(i, a_dictionary[i]))
