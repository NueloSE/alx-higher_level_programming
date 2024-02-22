#!/usr/bin/python3
"""
A module with as simple class Student

"""


class Student:
    """
    This class represents a student with attributes such as
    first name, last name and age.

    Attributes:
    first_name: A string representing the first name of the student.
    last_name: A string representing the last name of thes student.
    age: An integer representing the age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a student instance with firstname, lastname and age.
        Args:
            first_name: A string representing the first name of the student.
            last_name: A string representing the last name of thes student.
            age: An integer representing the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            If attrs is a list of strings, only attribute names contained
            in this list must be retrieved. Otherwise,
            all attributes must be retrieved
        """

        jsonAttrs = self.__dict__
        if attrs is None:
            return jsonAttrs

        self.reqAttrs = {}
        for i in range(len(attrs)):
            if attrs[i] in jsonAttrs:
                self.reqAttrs[attrs[i]] = jsonAttrs[attrs[i]]
        return self.reqAttrs
