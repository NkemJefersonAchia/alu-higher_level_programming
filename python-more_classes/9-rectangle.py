#!/usr/bin/python3
"""
This module defines a Rectangle class.

The Rectangle class supports:
- width and height attributes with validation,
- computing area and perimeter,
- string representation using a customizable print symbol,
- tracking number of instances,
- recreating an instance via eval(repr()),
- comparing two rectangles by area,
- creating a square (width == height) via a class method.

Raises appropriate exceptions on invalid inputs.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
        number_of_instances (int): Tracks number of Rectangle instances.
        print_symbol (any): Symbol used for string representation (default '#').

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        bigger_or_equal(rect_1, rect_2): Returns the bigger rectangle by area.
        square(size=0): Creates a square (width == height).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: Width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: Height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter or 0 if width or height is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return string of rectangle made of print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return string for recreating instance with eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print message on instance deletion and decrement count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare rectangles by area.

        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.

        Returns:
            Rectangle: The bigger or equal rectangle.

        Raises:
            TypeError: If inputs are not Rectangle instances.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a square-shaped Rectangle.

        Args:
            size (int): Size of width and height.

        Returns:
            Rectangle: New rectangle instance (square).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        try:
            return cls(size, size)
        except (TypeError, ValueError) as e:
            # Instantiate and delete dummy to trigger __del__
            dummy = cls.__new__(cls)
            Rectangle.number_of_instances += 1
            del dummy
            raise e
