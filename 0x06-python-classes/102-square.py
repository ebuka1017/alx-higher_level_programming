#!/usr/bin/python3

"""Define a square class."""


class Square:
    """Creates a square class object."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        """
        Initializes a square object with parameters.
        Size:

        Size (int) = size of the square
        """
        self.__size = size

    @property
    def size(self):
        """gets size"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """sets the size"""
        self.__size = size

    def area(self):
        """function returns the current square area"""
        return self.__size ** 2

    def __lt__(self, other):
        """less than"""
        return self.area() < other.area()

    def __gt__(self, other):
        """greater than"""
        return self.area() > other.area()

    def __ee__(self, other):
        """equal"""
        return self.area() == other.area()

    def __le__(self, other):
        """less than or equal to"""
        return self.area() <= other.area()

    def __ge__(self, other):
        """greater than or equal to"""
        return self.area() >= other.area()

    def __ne__(self, other):
        """not equal"""
        return self.area() != other.area
