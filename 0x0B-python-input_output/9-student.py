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

    def to_json(self):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the serialized
            attributes of the Student instance.
        """
        self.public_attribute = self.__dict__

        self.json_dict = {
            key: value for key, value in self.public_attribute.items()
            if (isinstance(value, (list, str, int, bool)))
        }

        return (self.json_dict)
