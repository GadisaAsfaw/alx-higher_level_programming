#!/usr/bin/python3
"""
This module defines a Square class initialise its size
Its implements value and type checks for its attributes
 Public instance method: def area(self).
"""


class Square:
    '''Class Square with private instance attribute size
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    '''
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size**2

    def my_print(self):
        """prints a square  with the corresponding size
        """
        if (self.__size == 0):
            print('')

        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
    pass
