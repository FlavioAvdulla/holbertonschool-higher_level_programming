#!/usr/bin/python3
"""
Animal Sounds Module
====================

This module demonstrates the use of abstract classes and method overriding in Python.

Classes
-------
Animal(ABC)
    Abstract base class for all animals.
Dog(Animal)
    Concrete subclass of Animal representing a dog.
Cat(Animal)
    Concrete subclass of Animal representing a cat.

Example
-------
>>> dog = Dog()
>>> cat = Cat()
>>> print(dog.sound())
Bark
>>> print(cat.sound())
Meow
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for all animals.

    Methods
    -------
    sound()
        Abstract method to be implemented by subclasses to define the sound the animal makes.
    """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """
    Concrete subclass of Animal representing a dog.

    Methods
    -------
    sound()
        Returns the sound that a dog makes.
    """
    def sound(self):
        return "Bark"
class Cat(Animal):
    """
    Concrete subclass of Animal representing a cat.

    Methods
    -------
    sound()
        Returns the sound that a cat makes.
    """
    def sound(self):
        return "Meow"
