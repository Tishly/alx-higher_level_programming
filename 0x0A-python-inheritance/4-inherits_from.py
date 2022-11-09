#!/usr/bin/python3


def inherits_from(obj, a_class):
    """
    A function that checks if the object is a child class of an instance
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
