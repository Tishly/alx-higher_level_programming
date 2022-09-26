#!/usr/bin/python3
"""

"""

from urllib.request import urlopen
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = urlopen(url)
    headers = response.info()
    print(response.headers['X-Request-Id'])
