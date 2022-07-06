#!/usr/bin/python3
"""Module 101-add_attribute.
Checks if an attribute can be added to an object.
"""


def add_attribute(*args):
    """adds a new attribute to an object if it’s possible"""

    if "main" in str(type(args[0])):
        setattr(args[0], args[1], args[2])
    else:
        raise TypeError("can't add new attribute")
