#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for i in matrix:
        sq_matrix.append([j ** 2 for j in i])
    return (sq_matrix)
