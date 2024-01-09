#!/usr/bin/python3
""" defines a Rectangle subclass Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Method for initializing a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
