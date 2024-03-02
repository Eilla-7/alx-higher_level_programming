#!/usr/bin/python3
"""
Script takes a URL as a command-line argument and sends a GET request to that
URL using the requests module

Usage:
    python3 5-hbtn_header.py <URL>

Arguments:
    <URL> : The URL from which to fetch the X-Request-Id header
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
