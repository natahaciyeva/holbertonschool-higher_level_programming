#!/usr/bin/python3
"""This module contains a function to check if an object is an instance
of a class. It also returns True if the object inherits from that class.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of it."""
    return isinstance(obj, a_class)
