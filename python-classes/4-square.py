#!/usr/bin/python3
"""Square class that defines a square by its size."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size  # Burada artıq setter işə düşəcək!

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
