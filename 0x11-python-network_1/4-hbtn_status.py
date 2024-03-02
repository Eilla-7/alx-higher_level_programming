#!/usr/bin/python3
"""
This script uses the requests module to send a GET request to the URL
"https://alx-intranet.hbtn.io/status" and prints information about the
response body
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
