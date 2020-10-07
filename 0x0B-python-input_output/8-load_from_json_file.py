#!/usr/bin/python3
"""
loads from json file
"""
import json


def load_from_json_file(filename):
    """loads from json file"""

    with open(filename, encoding="UTF-8") as f:
        return json.loads(f.read())
