#!/usr/bin/python3
"""
Script that If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""

from requests.exceptions import HTTPError
import requests as req
import sys

url = sys.argv[1]

try:
    response = req.get(url)
    print(response.text)
except HTTPError as e:
    if hassattr('e', 'code'):
        if e.code >= 400:
            print('Error code: ', e.code)
