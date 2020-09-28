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
        """initialises rectangle"""

        self.width = width
        self.height = height

    def perimeter(self):
        """returns the perimeter of a rectangle"""

        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def area(self):
        """returns the area of a rectangle"""

        return (self.__width * self.__height)

    @property
    def width(self):
        """property definition of width"""

        return self.__width

    @property
    def height(self):
        """property definition of height"""

        return self.__height

    @width.setter
    def width(self, value):
        """sets the width from given value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """sets the width from given value"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
