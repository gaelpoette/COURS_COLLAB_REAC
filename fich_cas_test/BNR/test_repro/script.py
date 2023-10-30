#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
from string import *
import os
import random
import matplotlib.pyplot as plt
import numpy as np


os.system("cp param.py ../../..")
os.system("python3 ../../../ode_mc.py")
os.system("cp rez.txt rez1.txt")
os.system("python3 ../../../ode_mc.py")
os.system("meld rez.txt rez1.txt")


