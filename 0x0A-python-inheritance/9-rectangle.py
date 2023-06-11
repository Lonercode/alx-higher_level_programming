#!/usr/bin/python3
""" Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Child class to BaseGeometry class"""

    def __init__(self, width, height):
        """Initalization"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height

    def area(self):
        """Area"""
        return self.width * self.height

    def __str__(self):
        """String"""
        return "[Rectangle] " + str(self.width) + "/" + str(self.height)
