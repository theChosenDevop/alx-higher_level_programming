#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    """
        Args:
            my_list: list of integers
            search: element to be found
            replace: element to be replaced with

        Returns:
            new_list
    """
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)

    return new_list
