#!/usr/bin/python3
"""Define write_file"""


def write_file(filename="", text=""):
    """write with utf-8"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
