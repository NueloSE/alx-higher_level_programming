#!/usr/bin/python3
"""
A Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
from sys import argv
import requests


def main():
    repoName = argv[1]
    ownerName = argv[2]
    url = f"https://api.github.com/repos/{repoName}/{ownerName}/commits"

    r = requests.get(url)

    if r.status_code == 200:
        commits = r.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')
    else:
        print(r.json())


if __name__ == "__main__":
    main()
