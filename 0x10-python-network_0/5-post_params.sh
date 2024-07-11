#!/bin/bash
#sending a post request
curl -sd POST  "email=test@gmail.com&subject=I will always be here for PLD" "$1"
