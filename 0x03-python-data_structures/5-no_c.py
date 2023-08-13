#!/usr/bin/python3

def no_c(my_string):
    x = []
    i = 0
    for c in my_string:
        i += 1
        if (c != 'c' and c != 'C'):
            x.append(c)
    return ''.join(x)
