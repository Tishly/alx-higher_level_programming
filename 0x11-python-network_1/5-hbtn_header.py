#!/usr/bin/python3
"""
Script that displays the value of the variable
X-Request-Id in the response header
"""

import requests as req
import sys

url = sys.argv[1]

if __name__ == '__main__':
    response = req.get(url)
    r = response.headers['X-Request-Id']
    print(r)
