#!/usr/bin/python3
"""Doc for class"""


class BaseGeometry:
    """BaseGeometry again"""


    def area(self):
        """Area Exception"""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """Validator"""
        self.value = value
        self.name = name
        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
