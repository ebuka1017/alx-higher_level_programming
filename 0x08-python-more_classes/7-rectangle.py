#!/usr/bin/python3
"""rectange class"""


class Rectangle:
    """makes rectangle object"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets width"""
        return self.__width

    @property
    def height(self):
        """gets height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            p = 0
            return p
        else:
            return ((2 * (self.__height)) + (2 * (self.__width)))

    def __str__(self):
        """modify str obj"""
        n = '\n'
        if self.__width == 0 or self.__height == 0:
            return ""
        return n.join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """modifies repr object

        """
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """signifies rectangle deletion"""
        print("{}".format("Bye rectangle..."))
        Rectangle.number_of_instances -= 1
