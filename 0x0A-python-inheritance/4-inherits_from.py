#!/usr/bin/python3
"""
module that checks if a object of a class is inherited from a class
"""


def inherits_from(obj, a_class):
    """
    function that ^
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
