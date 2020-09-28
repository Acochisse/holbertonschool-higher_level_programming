#!/usr/bin/python3
"""
This module defines a class Rectangle
Rectangle is defined by Height and Width
"""


class Rectangle:
    """
    class is defined by atr width and height:
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def area(self):
        return (self.__width * self.__height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

