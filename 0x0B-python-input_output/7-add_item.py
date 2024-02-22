#!/usr/bin/python3
"""
Simple adds command line argument in json format
to a json file called add_item.json
if add_item.json doesn't exit it creates it
if it exist it appends to it.
"""
import sys
loader = __import__('6-load_from_json_file').load_from_json_file
dumper = __import__('5-save_to_json_file').save_to_json_file


try:
    mylist = loader('add_item.json')
except Exception:
    with open("add_item.json", "w+", encoding='utf-8') as fileOpen:
        fileOpen.write("[]")

i = 1
mylist = loader('add_item.json')
while i < len(sys.argv):
    mylist.append(sys.argv[i])
    i += 1

dumper(mylist, 'add_item.json')
