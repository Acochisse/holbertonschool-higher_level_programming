#!/usr/bin/python3
"""
module of from_json_string
"""
import json


def from_json_string(my_str):
    """
    function that returns an object in JSON form
    """

    return json.loads(my_str)
