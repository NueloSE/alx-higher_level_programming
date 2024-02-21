#!/usr/bin/python3
import json
def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as openFile:
        json_obj = json.dump(my_obj, openFile)
