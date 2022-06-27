#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Instantiation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Private instance attribute
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise ("width nmust be an integer")
        if value < 0:
            raise ("width must be >= 0")
         self.__width = value
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise ("height nmust be an integer")
        if value < 0:
            raise ("height must be >= 0")
        self.__height = value
