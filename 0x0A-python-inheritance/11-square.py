#!/usr/bin/python3
""" defines a Rectangle subclass Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Rectangle:
   def __init__(self, width, height):
       self.width = width
       self.height = height

   def __str__(self):
       return f'[Rectangle] {self.width}/{self.height}'

class Square(Rectangle):
   def __init__(self, side):
       super().__init__(side, side)

   def __str__(self):
       return f'[Square] {self.width}/{self.width}'
