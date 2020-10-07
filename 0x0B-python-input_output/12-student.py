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
        artyom_dict = {}
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            for i, j in attrs:
                if i in self.__dict__.items():
                    if i in attrs:
                        artyom_dict[i] = j
                return artyom_dict
        else:
            return self.__dict__
