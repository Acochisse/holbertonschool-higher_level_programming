#!/usr/bin/python3
"""
function than inherits and sorts a list to return
"""


class MyList(list):
    """
    class Mylist
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        print (sorted_list)
