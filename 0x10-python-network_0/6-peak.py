def find_peak(list_of_integers):
    peak = 0
    for ind in list_of_integers:
        if ind > peak:
            peak = ind
        else:
            continue
    return (peak if peak != 0 else "None")
