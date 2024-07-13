#!/usr/bin/python3
"""
A  Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
"""

from sys import argv
import requests


def main():
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(argv) > 1:
        q = argv[1]
    data = {'q': q}

    try:
        r = requests.post(url, data=data)
        try:
            response = r.json()
            if response:
                id = response.get('id')
                name = response.get('name')
                print(f'[{id}] {name}')
            else:
                print('No result')
        except ValueError:
            print('Not a valid JSON')
    except requests.RequestException as e:
        print(f'Request failed: {e}')


if __name__ == "__main__":
    main()
