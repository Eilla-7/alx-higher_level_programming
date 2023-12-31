#!/usr/bin/python3
"""define save_to_json"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json"""
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
