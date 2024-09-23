#!/usr/bin/python3
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def __Str__(self):
        return f"[Rectabgle] {self.__width}/{self.__height}"