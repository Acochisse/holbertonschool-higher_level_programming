#!/usr/bin/python3
"""
module that converts into JSON string
"""
import json


def to_json_string(my_obj):
    """
    function that returns an object as a JSON string
    """

    return json.dumps(my_obj)
