#!/usr/bin/python3
'''
An add-integer function for a TDD project
Returns: the sum of two numbers.
They can be of type int or float.
'''


def add_integer(a, b=98):
    '''Computes the sum of two integers.
    Args:
        a (int): first integer.
        b (int, optional): second integer
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b'''

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
