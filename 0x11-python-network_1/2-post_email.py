#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""
from sys import argv
import urllib.request
import urllib.parse


def main():
    url = argv[1]
    email = argv[2]
    values = {
        'email': f'{email}'
    }
    data = (urllib.parse.urlencode(values)).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
    print(the_page)


if __name__ == "__main__":
    main()
