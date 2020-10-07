#!/usr/bin/python3
"""
module for class student
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """initialises the class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """creates a dict of Student attr"""

        if attrs is not None and all(isinstance(x, str) for x in attrs):
            b = {}
            for i, j in self.__dict__.items():
                if i in attrs:
                    b[i] = j
            return b
        else:
            return self.__dict__
