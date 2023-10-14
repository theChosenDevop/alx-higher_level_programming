#!/usr/bin/python3
# 100-weight_average.py

def weight_average(my_list=[]):
    """
        Args:
            my_list: list of integers

        Returns:
            weights average of all integers
    """

    if not my_list:
        return 0
    score = 0
    weight = 0

    for first, second in my_list:
        score = (first * second) + score
        weight = second + weight

    weighted_average = score / weight
    return weighted_average
