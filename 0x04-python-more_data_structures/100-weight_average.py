#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    top = list(map(lambda x: x[0] * x[1], my_list))
    sum_top = sum(top)

    den = list(map(lambda y: y[1], my_list))
    sum_den = sum(den)

    avg = sum_top/sum_den
    return avg
