#!/usr/bin/python3
"""
Script takes two command-line arguments: a URL and an email address

Usage:
    python3 2-post_email.py <URL> <EMAIL>

Arguments:
    <URL> : The URL to which the POST request will be sent
    <EMAIL> : The email address to be included in the POST request data
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
