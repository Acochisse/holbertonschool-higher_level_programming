#!/usr/bin/python3
"""
This module discribes a class without dynamically created atr
"""


class LockedClass:
    """
    Class with no atr
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        Initialises class
        """

        pass
