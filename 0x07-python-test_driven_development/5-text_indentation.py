#!/usr/bin/python3
"""
function that takes input poem and splits the text into a new line on separators
"""


def text_indentation(text):
    """
    function for above
    """

    characters = ['.', '?', ':']

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    buff = text.strip()

    for i, j in enumerate(buff):
        if j in characters:
            print("{:s}\n".format(j))
        else:
            if (buff[i - 1] in characters or \
                (buff[i] == ' ' and buff[i - 1] == ' ')):
                    continue
            print("{:s}".format(j), end="")
    print()
