#!/usr/bin/python3

def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return ("0")

    num, den = 0, 0

    for x in my_list:
        list(x)
        den += x[1]
        num += x[0] * x[1]

    avg = num / den

    return avg
