#!/usr/bin/python3
"""Script that serializes arguments passed to it

"""
import sys
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

list_str = None
list_obj = []
try:
    a_file = open("add_item.json", encoding="utf-8")
    list_str = a_file.read()
except FileNotFoundError:
    pass
else:
    a_file.close()

if list_str:
    list_obj = json.loads(list_str)

if sys.argv[1:]:
    list_obj.extend(sys.argv[1:])

with open("add_item.json", mode="w", encoding="utf-8") as a_file:
    json.dump(list_obj, a_file)
