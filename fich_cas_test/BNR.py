#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
from string import *
import os
import random
import matplotlib.pyplot as plt
import numpy as np


os.chdir("BNR/test_repro")
os.system("python3 test.py")
os.chdir("../..")

os.chdir("BNR/comp_codes")
os.system("python3 test.py")
os.chdir("../..")

os.chdir("BNR/unit_expo")
os.system("python3 test.py")
os.chdir("../..")

