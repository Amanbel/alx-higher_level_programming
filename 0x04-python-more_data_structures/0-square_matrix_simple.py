#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = 0
    m = 0
    new_list = []
    for i in matrix:
        for j in i:
            new_list[n][m] = list(map(lambda x: x**2, matrix[n]))
            m += 1
        n += 1
    return new_list
