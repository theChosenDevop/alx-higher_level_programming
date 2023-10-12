#!/usr.bin/python3
# 10-best_score.py

def best_score(a_dictionary):
    """best score function

        Args:
            a_dictionary: input

        Returns:
            score or None if not
    """
    if not a_dictionary:
        return None

    max_val = max(a_dictionary, key=a_dictionary.get)
    return max_val
