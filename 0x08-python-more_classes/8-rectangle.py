#!/usr/bin/python3
"""
This module defines a class Rectangle
Rectangle is defined by Height and Width
"""


class Rectangle:
    """
    class is defined by atr width and height:
    """
    number_of_instances = 0
    print_symbol = "#"

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

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return
        _print = ''
        for i in range(self.height):
            for j in range(self.width):
                _print += str(self.print_symbol)
            _print += '\n'
        _print = _print[:-1]
        return _print

    def __repr__(self):
        return "Rectangle({:d}, {:d}".format(self.__width, self.__height)

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2
