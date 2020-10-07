#!/usr/bin/python3
"""
module that reads and prints a file
"""


def read_file(filename=""):
    """ opens a defined file """

    with open("my_file_0.txt", encoding="UTF=8") as f:
        print(f.read())
