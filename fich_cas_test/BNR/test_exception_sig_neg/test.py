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
ref = "ATTENTION! Les constantes de reaction doivent etre positif\n"
for line in f:
    #print(line)
    #print(ref)
    if line == ref:
        print(" ------------------------             test OK  --------------------------------")
    else:
        print(" ------------------------             test KO  --------------------------------")






