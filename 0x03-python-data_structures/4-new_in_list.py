#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list
    if idx < 0 or idx >= my_list[idx]:
        return copy
    else:
        my_list = list(my_list)
        my_list[idx] = element
        return my_list
