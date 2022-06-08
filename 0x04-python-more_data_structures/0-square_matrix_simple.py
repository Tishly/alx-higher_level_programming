#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    result = [list(map((lambda x: x*x), element)) for element in matrix]
    return result
'''
rows, cols = len(new_matrix), len(new_matrix[0])
    for i in range(rows):
                for j in range(cols):
                                newMatrix = list(map(lambda x: x*x, new_matrix))
                                            print(newMatrix)
'''
