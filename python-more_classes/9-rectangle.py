#!/usr/bin/python3
"""
Rectangle Module

Defines a Rectangle class with width and height attributes.
"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
    number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
        width (int): The width of the rectangle. Default is 0.
        height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
        value (int): The width of the rectangle.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
        value (int): The height of the rectangle.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
        int: The perimeter, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the rectangle as a string of `#` characters.

        Returns:
        str: The rectangle, or an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        new_string = ""

        for i in range(self.__height):
            new_string += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                new_string += "\n"
        return new_string

    def __repr__(self):
        """
        Returns a string representation of the rectangle for debugging.

        Returns:
        str: A string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rectangle or rect_1 if equal.

        Args:
        rect_1 (Rectangle): First rectangle.
        rect_2 (Rectangle): Second rectangle.

        Raises:
        TypeError: If rect_1 or rect_2 is not a Rectangle.

        Returns:
        Rectangle: The rectangle with the greater area, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a square rectangle.

        Args:
        size (int): Size of the square sides.

        Returns:
        Rectangle: New instance with width and height equal to size.
        """
        return cls(size, size)
