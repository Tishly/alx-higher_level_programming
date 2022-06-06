#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        matrix_T.append(row)
    print("{}".format(matrix_T))
