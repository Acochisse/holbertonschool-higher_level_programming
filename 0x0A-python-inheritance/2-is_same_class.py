#!/usr/bin/python3
"""
module that tests if the class of two objects is the same
"""


def is_same_class(obj, a_class):
    """
    checks if object is same class
    """

    return type(obj) is a_class
