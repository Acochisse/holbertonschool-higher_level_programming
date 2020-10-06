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
