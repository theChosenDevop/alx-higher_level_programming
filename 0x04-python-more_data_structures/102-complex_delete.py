#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    
        Args: 
            a_dictionary: dictionary
            value: value of dictionary key

        Returns:
                dictionary
    """
    filtered_dict = {k: v for k, v in a_dictionary.items() if v != value}
    return filtered_dict
