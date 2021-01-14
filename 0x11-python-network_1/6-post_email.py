#!/usr/bin/pyhon3
"""
script
"""
import requests
from sys import argv


if __name__ == '__main__':
    posting = {'email': argv[2]}
    r = requests.post(argv[1], data=posting)
    print(r.text)
