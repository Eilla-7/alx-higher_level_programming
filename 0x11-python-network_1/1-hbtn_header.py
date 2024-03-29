#!/usr/bin/python3
"""
Script takes a URL as a command-line argument and sends a request to that
URL using the urllib module

Usage:
    python3 1-hbtn_header.py <URL>
Arguments:
    <URL> : The URL from which to fetch the X-Request-Id header
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
