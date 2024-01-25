""" Defines find_peak function """
def find_peak(list_of_integers):
    """  finds a peak in a list of unsorted integers. """
    peak = 0
    for ind in list_of_integers:
        if ind > peak:
            peak = ind
        else:
            continue
    return (peak if peak != 0 else "None")
