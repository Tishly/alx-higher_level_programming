#!/usr/bin/python3
'''
A python function
'''


def lookup(obj):
    '''
    Function to display attributes and
    methods of an object
    Args:
        obj
    Return:
        A list called list
    '''
    list = dir(obj)
    return list
