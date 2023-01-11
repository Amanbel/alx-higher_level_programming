#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            new_list[i] = list(map(lambda x: x**2, matrix[i]))
    return new_list
