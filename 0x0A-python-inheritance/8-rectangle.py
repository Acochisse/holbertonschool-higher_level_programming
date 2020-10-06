#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry():
    """
    Class BaseGeometry
    """

    def area(self):
        """Calculates area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates input type int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    class Rectangle inherits from clas BaseGeo
    """

    def __init__(self, width, height):
        """frame"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
