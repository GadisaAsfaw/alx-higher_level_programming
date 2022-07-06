#!/usr/bin/python3
"""Module 100-my_int.
Creates a class that inherits from int.
"""


class MyInt(int):
    """Class inheriting from int,
    But reverses the behavior of != and ==.
    """

    def __init__(self, value):
        self.num = value

    def __eq__(self, other):
        return self.num != other

    def __ne__(self, other):
        return self.num == other
