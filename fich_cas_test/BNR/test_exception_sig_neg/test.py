#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
from string import *
import os
import random
import matplotlib.pyplot as plt
import numpy as np


print(" TEST POSITIVITÉ DES SIGMA ")
os.system("cp param.py ../../..")
os.system("python3 ../../../ode_mc.py > listing")

f = open("listing", 'r')
for line in f:
    #print(line)
    if line == "ATTENTION! Les constantes de reaction doivent etre positif":
        print(" ------------------------             test OK  --------------------------------")
    else:
        print(" ------------------------             test KO  --------------------------------")






