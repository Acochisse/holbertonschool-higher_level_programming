#!/usr/bin/python3
"""
module that returns the number of lines in a text file
"""


def read_lines(filename="", nb_lines=0):
    """reads the file and returns the specified number of lines"""

    with open("my_file_0.txt", encoding='UTF-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for i in range(nb_lines):
            print(f.readline(), end="")
