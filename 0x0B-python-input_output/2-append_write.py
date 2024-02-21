#!/usr/bin/python3
"""
Module: 1-write_file

This module provides functions for writing to files.
"""


def append_write(filename="", text=""):
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
    with open(filename, "+a", encoding='utf-8') as openFile:
        count = openFile.write(text)
    return count
