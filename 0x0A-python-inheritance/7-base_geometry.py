#!/usr/bin/python3
""" A place holder class """


class BaseGeometry:
    """ An empty class """
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be a greater than 0".format(name))
