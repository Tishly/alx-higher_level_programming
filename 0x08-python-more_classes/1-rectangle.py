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
        try:
            if isinstance(value, int) and value >= 0:
                self.__width = value
        except TypeError:
            raise ("width nmust be an integer")
        except ValueError:
            raise ("width must be >= 0")
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if isinstance(value, int) and value >= 0:
                self.__height = value
        except TypeError:
            raise ("height nmust be an integer")
        except ValueError:
            raise ("height must be >= 0")
