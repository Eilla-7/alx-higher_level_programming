#!/usr/bin/python3
"""
Sends a POST request with email data to a specified URL
using the requests module

Usage:
    python3 script.py <URL> <EMAIL>

Arguments:
    <URL> : The URL to which the POST request will be sent
    <EMAIL> : The email address to be included in the POST request data
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
