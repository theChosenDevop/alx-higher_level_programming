#!/usr/bin/python3

def best_score(a_dictionary):
    """ best score function

        Args:
            a_dictionary: dictionary

        Returns:
            A key with the biggest integer value
    """
    max_val = 0
    best_key = None
    if  not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > max_val:
            max_val = value
            best_key = key

    return (best_key)
