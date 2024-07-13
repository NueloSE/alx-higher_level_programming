#!/usr/bin/python3
"""
A  Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token as password
to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access
token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth


def main():
    username = argv[1]
    pat = argv[2]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=HTTPBasicAuth(username=username, password=pat))
    response = r.json()
    if response:
        print(f"{response['id']}")


if __name__ == "__main__":
    main()
