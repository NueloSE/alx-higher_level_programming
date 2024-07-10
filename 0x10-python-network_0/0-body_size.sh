#!/bin/bash
# A script that takes in a URL sends a request to the URL
echo "$(curl -s -w '%{size_download}' $1)"
