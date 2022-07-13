#!/usr/bin/python3
'''
Contains lookup function
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


class MyList(list):
    '''
    A subclass inheriting from list
    '''
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
