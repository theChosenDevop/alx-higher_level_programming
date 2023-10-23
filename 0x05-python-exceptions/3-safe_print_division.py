#!/usr/bin/python3

def safe_print_division(a, b):
    """
        safe_print_division
            function that divides 2 integers and prints the result

        Args:
            a: integer
            b: integer

        Return:
            the value of the division, otherwise: None
    """
    try:
        outcome = a / b
    except (TypeError, ZeroDivisionError):
        outcome = "None"
    finally:
        print("Inside result: {}".format(outcome))
    return outcome
