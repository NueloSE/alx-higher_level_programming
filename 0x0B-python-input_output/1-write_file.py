#!/usr/bin/python3
"""
Module: 1-write_file

This module provides functions for writing to files.
"""


def write_file(filename="", text=""):
    """
    ``write_file`` function write to a file,
    Truncates the file if it exist
    Creates the filename if it does not exit

    Args:
        filename (str): The name of the file to write to.
        Default value set to an empty string.
        text (str): The text to be written to the filename.
        Default value set to an empty string.

    Returns:
        Number of character written to the file

    Raises:
        No Exceptions
    """
    count = 0
    with open(filename, "w", encoding='utf-8') as file_open:
        count = file_open.write(text)
    return count
