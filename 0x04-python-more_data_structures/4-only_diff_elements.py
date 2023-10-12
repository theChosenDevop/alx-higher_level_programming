#!/usr/bin/python3
# 4-only_diff_elements.py

def only_diff_elements(set_1, set_2):
    """ only different elements function
        Args:
            set_1: first set
            set_2: second set

        Returns:
            diference elemnent in two sets but not both

    """
    return set_1 ^ set_2
