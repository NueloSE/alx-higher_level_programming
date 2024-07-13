#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
You are not allow to import other packages than requests and sys
The value of this variable is different for each request
You don’t need to check script arguments (number and type)
"""

from sys import argv
import requests


def main():
    url = argv[1]
    req = requests.get(url)
    head = req.headers

    for key, value in head.items():
        if key == "X-Request-Id":
            print(value)


if __name__ == "__main__":
    main()
