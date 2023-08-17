#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    def square(x):
        return x**2
    res = []

    for row in matrix:
        squared = list(map(square, row))
        res.append(squared)
    return res
