#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area() method.
The area() method is not implemented and raises an Exception.
"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
