#!/usr/bin/python3
"""
module that reads and prints a file
"""


def read_file(filename=""):
    """ opens a defined file """

    with open(filename, 'r') as f:
        read = f.read()
        print(read, end="")
