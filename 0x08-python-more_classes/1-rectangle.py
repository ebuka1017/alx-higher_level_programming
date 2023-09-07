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
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        """sets the width"""
        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        """sets the height"""
        self.__height = value
