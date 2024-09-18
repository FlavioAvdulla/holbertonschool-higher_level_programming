#!/usr/bin/python3

class Square:

        self.size = size

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        [print()for _ in range(position[1])]
        for i in range(self.size):
            print(" " * self.__position[0] + "#" * self.__size)
