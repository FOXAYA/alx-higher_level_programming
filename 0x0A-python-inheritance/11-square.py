#!/usr/bin/python3


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Method for initializing a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Method that returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
