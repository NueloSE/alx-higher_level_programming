#!/usr/bin/python3
"""
Module: 0-read_file

This module provides functions for reading files.
"""


def read_file(filename=""):
    """
    ``read_file`` function reads the content of a file,
    and prints each line to the stdout

    Args:
        filename (str): The name of the file to read.
        Default value set to an empty string.

    Returns:
        None

    Raises:
        None for now
    """
    with open(filename, "r", encoding='utf-8') as file_open:
        for line in file_open:
            print(line, end="")
