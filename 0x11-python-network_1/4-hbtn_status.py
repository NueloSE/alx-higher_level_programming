#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following
example (tabulation before -)
"""
import requests


def main():
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    output = 'Body response:\n\t- type: {}\n\t- content: {}'
    print(output.format(type(req.text), req.text))


if __name__ == "__main__":
    main()
