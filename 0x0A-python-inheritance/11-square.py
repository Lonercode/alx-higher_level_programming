#!/usr/bin/python3
"""Square again"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.size = size

    def area(self):
        """Area of square"""
        return self.size ** 2

    def __str__(self):
        """String"""
        return "[Square] " + str(self.size) + "/" + str(self.size)
