#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
from string import *
import os
import random
import matplotlib.pyplot as plt
import numpy as np


print(" VERIFIFACTION DE TYPE DE REACTION ")
os.system("cp param.py ../../..")
os.system("python3 ../../../ode_mc.py > listing")

f = open("listing", 'r')
ref = "ATTENTION! ce type de reaction n'existe pas \n"
for line in f:
    #print(line)
    #print(ref)
    if line == ref:
        print(" ------------------------             test OK  --------------------------------")
    else:
        print(" ------------------------             test KO  --------------------------------")






