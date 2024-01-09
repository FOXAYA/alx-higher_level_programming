#!/usr/bin/python3
class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a nهew square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
