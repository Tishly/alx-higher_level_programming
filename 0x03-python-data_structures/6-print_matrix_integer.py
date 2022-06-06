#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for index, item in enumerate(matrix, start=1):
        print("{}".format(item))
        if not index % 3:
            print("{}".format(index))
