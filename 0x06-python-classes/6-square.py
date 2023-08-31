#!/usr/bin/python3

"""Define a square class."""


class Square:
    """Creates a square class object."""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        """
        Initializes a square object with parameters.
        Size:

        Size (int) = size of the square
        position (tuple) = represents new position
        """
        self.__size = size
        self.__position = position

    def area(self):
        """function returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """gets size"""
        return self.__size

    @property
    def position(self):
        """gets position"""
        return self.__position

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """sets the size"""
        self.__size = size

    @position.setter
    def position(self, value):
        """sets the position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        x,y = value

        if not isinstance(x, int) or not isinstance(y, int) or (x < 0) or (y < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints square to stdout"""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print("{} ".format(" " * self.__position[0] + '#' * self.__size))
