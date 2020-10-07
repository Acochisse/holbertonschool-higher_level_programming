#!/usr/bin/python3
"""
module to save to json
"""
import json


def save_to_json_file(my_obj, filename):
    """function that converts obj into json"""

    with open(filename, "w", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
