#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
from string import *
import os
import random
import matplotlib.pyplot as plt
import numpy as np

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        if f1.read() == f2.read():
            return "The tests are identical"
        else:
            return "The tests are not identical"

os.system("cp param.py ../../..")
os.system("python3 ../../../ode_mc.py")
os.system("cp rez.txt rez1.txt")
os.system("python3 ../../../ode_mc.py")
comparison_result = compare_files("rez.txt", "rez1.txt")
print("\n----------\n" + comparison_result + "\n----------\n")

#os.system("meld rez.txt rez1.txt")
#os.system("diff rez.txt rez1.txt")
os.system("rm -f rez.txt rez1.txt gnu.plot")
#print("\n----------\n" + comparison_result + "\n----------\n")
