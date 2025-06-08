#!/usr/bin/python3
"""
This is a script that adds all arguments
to a Python list, and then save them to a file
"""
import json
import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file = "add_item.json"

if os.path.exists(file):
    items = load_from_json_file(file)
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, file)
