#!/usr/bin/python3
"""
Searches for a user based on a letter using a POST request

Usage:
    python3 8-json_api.py [<LETTER>]

Arguments:
    [<LETTER>] : A single letter to search for a user. If not provided,
                 all users will be searched
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
