#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""
from sys import argv
import urllib.request


def main():
	url = argv[1]
	req = urllib.request.Request(url)
	try:
		urllib.request.urlopen(req)
	except urllib.error.HTTPError as e:
		print(f"Error code: {e.code}")



if __name__ == "__main__":
	main()
