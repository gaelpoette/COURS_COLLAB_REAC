#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# Prints the current working directory
print(f"Current working directory: {os.getcwd()}")

files_to_remove = [
    "BNR/comp_codes/rez_det.txt",
    "BNR/comp_codes/rez_mc.txt",
    "BNR/comp_codes/rez.txt",
    "BNR/comp_codes/gnu.plot",
    "BNR/test_repro/output.png",
    "BNR/comp_codes/output.png",
    "../gnu.plot",
]

for file_path in files_to_remove:
    # Generate the absolute path
    abs_file_path = os.path.abspath(file_path)
    print(f"Checking: {abs_file_path}")

    # Check if the file exists at the absolute path
    if os.path.exists(abs_file_path):
        print(f"Removing: {abs_file_path}")
        os.remove(abs_file_path)
    else:
        print(f"File not found, did not remove: {abs_file_path}")
