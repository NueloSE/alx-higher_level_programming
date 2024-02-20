#!/usr/bin/python3
"""
A module containing a function that prints a string with 2 arguments to stdout.

The ``say_my_name`` function takes first_name and last_name(option),
if passed with only first_name default "" is set for last_name
it prints 'My name is <first name> <last name>' to the stdout

Example:
    say_my_name("John", "Smith")
Output:
    "My name is John Smith"
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string to the stdout

    Args:
        first_name: A string containing the user firstname
        last_name: A string containing the user lastname
    Raises:
        TypeError: if firstname or lastname not a string


    Returns:
        nothing just prints to the stdout
    """
    er = "say_my_name() missing 1 required positional argument: 'first_name'"
    if (first_name == ""):
        raise TypeError(er)
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
