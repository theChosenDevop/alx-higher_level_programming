#!/usr/bin/python3
# 100-weight_average.py

def weight_average(my_list=[]):
    """
        Args:
            my_list: list of integers

        Returns:
            weights average of all integers
    """
    return list(map([lambda x: x + y for x, y in my_list]))
