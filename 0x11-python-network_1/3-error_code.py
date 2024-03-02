#!/usr/bin/python3
"""Script takes a URL as a command-line argument and attempts to fetch its
content using the urllib module

Usage:
    python3 3-error_code.py <URL>

Arguments:
    <URL> : The URL whose content will be fetched
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
