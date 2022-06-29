#!/usr/bin/python3
'''Contains an add-integer function for a TDD project
'''


def add_integer(a, b=98):
    '''Computes the sum of two integers.
    Args:
        a (int): first integer.
        b (int, optional): second integer.
    Returns:
        int: sum of two integers.'''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
