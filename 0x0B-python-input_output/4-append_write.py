#!/usr/bin/python3
"""
module that appends a file a file
"""


def append_write(filename="", text=""):
    """writes txt to file under the name filename"""

    with open(filename, mode="a", encoding="UTF-8") as f:
        return f.write(text)
