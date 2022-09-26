#!/usr/bin/python3
"""
A script that sends an email with POST through email variable
"""

from urllib.request import urlopen
import urllib.parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    e_address =  sys.argv[2]
    values = {'email': 'e_address'}
   """ data = urllib.parse.urlencode(values)
    data = data.encode('utf8')"""
    req = urllib.request.Request(url, data)
    with urlopen(req) as response:
        headers = response.info()
        print('Your email is: {}'.format(response.headers['email']))
