#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """
        Args:
            tuple_a: empty tuple
            tuple_b: empty tuple

        Return:
            new tuple
    """
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)
    sum_1 = a[0] + b[0]
    sum_2 = a[1] + b[1]

    return (sum_1, sum_2)
