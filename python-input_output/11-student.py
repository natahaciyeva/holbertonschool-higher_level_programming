#!/usr/bin/python3
"""Module that defines a Student class with serialization/deserialization."""


class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the Student instance.

        If attrs is a list of strings, only include those attributes.
        """
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance using the json dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
