#!/usr/bin/python3
"""
Fetches the content of a URL using the requests module

Usage:
    python3 7-error_code.py <URL>

Arguments:
    <URL> : The URL from which to fetch the content
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
