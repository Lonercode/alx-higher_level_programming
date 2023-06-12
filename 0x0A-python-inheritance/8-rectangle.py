#!/usr/bin/python3
"""BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry"""


    def __init__(self, width, height):
        """Initilaization"""
        self.width = width
        self.height = height
        self.integer_validator("width", self.width)
        self.integer_validator("height", self.height)
