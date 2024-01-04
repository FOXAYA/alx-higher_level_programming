#!/usr/bin/python3
""" defines a Rectangle class"""


class Rectangle:
    """Rectangle Class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Init Method """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter def"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter def"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter def"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter def"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """define area def"""
        return self.__width * self.__height

    def perimeter(self):
        """define perimeter def"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """define informal print str"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            hsh = str(self.print_symbol)
            return ((hsh*self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        """define official print repr"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """define delete method"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Biggest Rectangle (Rectangle)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        Area1 = rect_1.area()
        Area2 = rect_2.area()
        if Area1 >= Area2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance """
        return (cls(size, size))
