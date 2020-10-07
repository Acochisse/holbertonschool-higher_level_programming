#!/usr/bin/python3
"""
creates a new class json
"""


def class_to_json(obj):
    """function that returns a dict with obj structure"""

    return obj.__dict__
