#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """ Rectangle class with
     attribute width and height,
     and getter and setter
"""
    def __init__(self, width=0, height=0):
        """ initializes a class
        Args:
         width
         height

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets new width value"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >=0 ')
        self.__width = value

    @property
    def height(self):
        """Returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets new height value """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >=0 ')
        self.__height = value
