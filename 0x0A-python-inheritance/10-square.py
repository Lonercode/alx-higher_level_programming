#!/usr/bin/python3

"""Square """

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """Initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.size = size

    def area(self):
        """Return the area"""
        return self.size ** 2
