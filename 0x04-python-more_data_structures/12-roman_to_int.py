#!/usr/bin/python3
# 12-roman_to_int.py

def roman_to_int(roman_string):
    """
        Args:
            roman_to_string: Roman letter to be converted

        Returns: value for each Roman letter
    """
    if not isinstance(roman_string, str):
        return 0
    if not roman_string:
        return 0
    rom_values = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = rom_values.get(char, 0)

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total
