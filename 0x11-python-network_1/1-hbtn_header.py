#!/usr/bin/python3
"""
Module that reads a url and displays value of header
"""
from sys import argv
import urllib.request as request


if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
