#!/usr/bin/python3
"""
Module that finds the peak of an array
"""


def find_peak(list_of_integers):
    """ function to find peak """

    list1 = list_of_integers
    if not list1:
        return None

    if len(list1) >= 1:
        if list1[0] >= list1[1]:
            return list1[1]
        if list1[-1] >= list1[-2]:
            return list1[-1]
        for x in range(len(list1)):
            if list1[x] > list1[x-1] and list1[x] > list1[x+1]:
                return list1[x]
    return list1[0]
