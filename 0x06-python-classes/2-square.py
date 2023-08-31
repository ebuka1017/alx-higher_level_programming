#!/usr/bin/python3

"""Define a square class."""


class Square:
    """Creates a square class object."""

    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        """
        Initializes a square object with parameters.
        Size:

        Size (int) = size of the square
        """
        self.size = size
