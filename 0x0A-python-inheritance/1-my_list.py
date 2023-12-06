#!/usr/bin/python3
"""MyList class' Module"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
