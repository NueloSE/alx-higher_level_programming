#!/bin/bash
#list all allowed method
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
