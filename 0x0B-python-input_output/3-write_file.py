#!/usr/bin/python3
"""
module that writes a file
"""


def write_file(filename="", text=""):
    """writes txt to file under the name filename"""

    with open(filename, "w") as f:
        return f.write(text)
