#!/usr/bin/python3
"""module for a function"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


lst = []

try:
    lst = list(load_from_json_file("add_item.json"))
except:
    len(lst) == 0

for i in range(1, len(argv)):
    lst.append(argv[i])

save_to_json_file(lst, "add_item.json")
