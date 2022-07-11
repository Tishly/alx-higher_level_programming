#!/usr/bin/python3



def matrix_divided(matrix, div):
    '''
    Args:
        matrix (int/float): list of lists to be divided
        div (int/float): denominator'''
    for row in matrix:
        for value in row:
    if not isinstance(matrix[], (int, float)):
        raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    if not len(matrix[]):
        raise TypeError ("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError ("div must be a number")
    if div = 0:
        raise ZeroDivisionError ("division by zero")
    return (lambda x: x /div for x in matrix)
    
