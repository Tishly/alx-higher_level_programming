#!/usr/bin/python3
"""
A class that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    Args:
    width - the width of the triangle
    height - the height of the triangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
