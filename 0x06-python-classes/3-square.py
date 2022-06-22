#!/usr/bin/python3
"""
This module defines a Square class initialise its size
Its implements value and type checks for its attributes
 Public instance method: def area(self).
"""


class Square:
    '''Class Square with private instance attribute size
    '''
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size**2
    pass
