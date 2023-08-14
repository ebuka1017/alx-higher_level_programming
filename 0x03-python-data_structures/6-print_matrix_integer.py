#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    s = ' '
    for x in matrix:
        for y in x:
            print("{}".format(y), end=' ')
        print("{}".format(s))
