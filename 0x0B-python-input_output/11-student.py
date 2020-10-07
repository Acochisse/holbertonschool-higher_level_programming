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

    def to_json(self):
        """creates a dict of Student attr"""
        return self.__dict__
