#!/usr/bin/python3
""" Defines add_item function  adds all arguments to a python
    list and a=save them into a file"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.py"

try:
    file2 = load_from_json_file(filename)
except FileNotFoundError:
    file2 = []

for args in argv[1:]:
    file2.append(args)

save_to_json_file(file2, filename)
