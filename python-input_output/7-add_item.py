#!/usr/bin/python3
import sys
from os.path import exists

# Import your functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if the file exists and load the data, otherwise start with an empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Append new arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)

