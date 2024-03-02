#!/usr/bin/python3
"""
Fetches the GitHub user ID using HTTP basic authentication

Usage:
    python3 10-my_github.py <USERNAME> <PASSWORD>

Arguments:
    <USERNAME> : The GitHub username used for authentication.
    <PASSWORD> : The GitHub password used for authentication.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
