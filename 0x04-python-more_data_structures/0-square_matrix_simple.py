#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        for x in i:
            square_matrix = list(map(lambda x: x*x, i))
        new_matrix.append(square_matrix)
    return(new_matrix)
