#!/usr/bin/python3
"""
module that returns the number of lines in a text file
"""


def number_of_lines(filename=""):
    """reads and then returns number of lines"""

    with open("my_file_0.txt", 'r') as f:
        lines = 0
        for line in f:
            lines += 1
        return lines
