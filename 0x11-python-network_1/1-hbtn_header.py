#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response.

You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed to the script (number or type)
You must use a with statementWrite a Python script that takes in a URL,
sends a request to the URL and displays the value of the X-Request-Id
variable found in the header of the response.

You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed to the script (number or type)
You must use a with statement
"""
from sys import argv
from urllib.request import urlopen


def fetch_id(url):
    with urlopen(url) as response:
        headers = response.getheaders()
    for head in headers:
        if head[0] == "X-Request-Id":
            print(head[1])


def main():
    fetch_id(argv[1])


if __name__ == "__main__":
    main()
