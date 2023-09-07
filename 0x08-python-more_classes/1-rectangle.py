#!/usr/bin/python3

"""
    Rectangle class
"""


class Rectangle:
    """create a rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle object with parameters.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """returns width"""
        return self.__width

    @property
    def height(self):
        """returns height"""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        """sets the width"""
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        """sets the height"""
        self.__height = value
