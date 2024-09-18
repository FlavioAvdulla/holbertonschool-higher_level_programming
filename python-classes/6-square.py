#!/usr/bin/python3
class Square:
    """
    A class to represent a square.

    Attributes:
    -----------
    size : int
        The size of the square's side.
    position : tuple
        The position of the square for printing.

    Methods:
    --------
    area():
        Returns the area of the square.
    my_print():
        Prints the square with the character '#'.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position.

        Parameters:
        -----------
        size : int, optional
            The size of the square's side (default is 0).
        position : tuple, optional
            The position of the square for printing (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
        --------
        int
            The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        -----------
        value : int
            The size of the square's side.

        Raises:
        -------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
        --------
        tuple
            The position of the square for printing.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
        -----------
        value : tuple
            The position of the square for printing.

        Raises:
        -------
        TypeError
            If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        --------
        int
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return
        for y in range(self.position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
