#!/usr/bin/python3
"""
function that adds two integers
requires input of int or float
will default to 98 for position b if only one arg (a)
"""


def add_integer(a, b=98):
    """
    adds two integers
    requires an imput of float or int type for a and b args
    returns the sum
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError(' bmust be an integer')

    return int(a) + int(b)
