#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
        list_division
            function that divides element by element 2 lists

        Args:
            my_list_1: first list
            my_list_2: second list
            list_length: length of list

        Return:
            new list of divided list
    """
    new_list = []
    for element in range(list_length):
        try:
            div = my_list_1[element] / my_list_2[element]
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except TypeError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            new_list.append(div)

    return new_list
