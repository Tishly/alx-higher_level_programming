#!/usr/bin/python3
"""
Script to manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""

from urllib.request import Request, urlopen
import sys
from urllib.error import HTTPError

url = sys.argv[1]
req = Request(url)
try:
    repsonse = urlopen(url)
except HTTPError as e:
    if hasattr(e, 'code'):
        print('Error code:', e.code)
