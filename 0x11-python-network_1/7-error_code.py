#!/usr/bin/python3
"""
Script that If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""

from requests.exceptions import HTTPError
import requests as req
import sys

url = sys.argv[1]

res = req.get(url)
if res.status_code == 200:
    print(res.text)
if res.status_code >= 400:
    print('Error code: {}'.format(res.status_code))
