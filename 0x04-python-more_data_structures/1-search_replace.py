#!/usr/bin/python
def search_replace(my_list, search, replace):
    new = [replace if i == search else i for i in my_list]
    return new
