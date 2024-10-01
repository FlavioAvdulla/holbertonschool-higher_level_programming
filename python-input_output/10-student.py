#!/usr/bin/python3
"""
student_module.py

This module defines the Student class,
which represents a student with a first name,
last name, and age.
"""


class Student:
    """
    A class used to represent a Student.

    Attributes
    ----------
    first_name : str
        The first name of the student.
    last_name : str
        The last name of the student.
    age : int
        The age of the student.

    Methods
    -------
    to_json():
        Returns a dictionary representation of the
        student's attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructs all the necessary attributes
        for the student object.

        Parameters
        ----------
        first_name : str
            The first name of the student.
        last_name : str
            The last name of the student.
        age : int
            The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation
        of the student's attributes.

        Returns
        -------
        dict
            A dictionary containing the student's
            first name, last name, and age.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        """
        attrs : list, optional
            A list of attribute names to retrieve (default is None).

        Returns
        -------
        dict
            A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
