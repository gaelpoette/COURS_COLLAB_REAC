#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
from string import *
import os
import random
import matplotlib.pyplot as plt
import numpy as np


os.chdir("BNR/test_repro")
os.system("cp param.py ../../..")
os.system("python3 script.py")
os.chdir("..")

