#!/usr/bin/python3
"""
function that prints a square
"""


def print_square(size):
    """
    prints a square based on dimensions given in size
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if not isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    if isinstance(size, int) and size > 0:
        for i in range(size):
            for j in range(size - 1):
                print('#', end="")
            print('#')
