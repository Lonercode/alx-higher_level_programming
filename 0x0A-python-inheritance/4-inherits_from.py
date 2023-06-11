#!/usr/bin/python3
"""If inherits from class"""
def inherits_from(obj, a_class):
    """Find out if inherits from class"""
    return isinstance(obj, a_class) and type(obj) != a_class
