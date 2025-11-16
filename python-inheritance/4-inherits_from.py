#!/usr/bin/python3
"""Module to check if an object is a subclass of a specified class.
It returns True only if the object is a subclass, not the same class.
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited from
    a_class (not the same class)."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
