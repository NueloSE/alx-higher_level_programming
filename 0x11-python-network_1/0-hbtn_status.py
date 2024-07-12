#!/usr/bin/python3
"""
A python script that fetches https://alx-intranet.hbtn.io/status
- You must use the package urllib
- You are not allowed to import any packages other than urllib
- The body of the response must be displayed like the following
example (tabulation before -)
- You must use a with statement
"""

import urllib.request

if __name__ == "__main__":
    urlToFetch = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(urlToFetch) as response:
        html = response.read()
    output = "Body response:\n\t- "\
             "type: {}\n\t- "\
             "content: {}\n\t- "\
             "utf content: {}"
    print(
        output.format(type(html), html, html.decode('utf-8'))
    )
