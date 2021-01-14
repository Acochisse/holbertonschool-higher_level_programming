#!/usr/bin/python3
"""
script
"""
import requests


if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    info = r.text
    print("Body response:")
    print("\t- type: {}".format(type(info)))
    print("\t- content: {}".format(info))
