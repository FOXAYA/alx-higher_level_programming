#!/usr/bin/python3
"""
    7-base_geometry.py
"""


class BaseGeometry:
    """BaseGeometry class"""

    def integer_validator(self, name, value):
        """Method for validate if a num is integer"""
        if type(value) != int:
            raise TypeError(name + " " + "must be an integer")
        if value <= 0:
            raise ValueError(name + " " + "must be greater than 0")
