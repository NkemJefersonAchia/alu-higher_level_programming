#!/usr/bin/python3
"""BaseGeometry class with integer validation."""


class BaseGeometry:
    """Base class for geometry operations."""
    
    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate a value as a positive integer.
        
        Args:
            name: Name of the value (string).
            value: Value to validate.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
