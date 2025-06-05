#!/usr/bin/python3
"""
This module provides the Student class that
converts a Student object to its JSON representation
"""


class Student:
    """
    A class that defines a student by their first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of the Student instance"""
        return self.__dict__