#!/usr/bin/python3
""" MyInt """


class MyInt(int):
    """MyInt"""


    def __ne__(self, sec):
        """int"""
        return super().__eq__(sec)


    def __eq__(self, sec):
        """int"""
        return super().__ne__(sec)
