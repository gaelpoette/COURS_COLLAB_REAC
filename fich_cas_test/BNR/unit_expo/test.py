#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
from string import *
import os
import random
import matplotlib.pyplot as plt
import numpy as np
from param import *
import sys
import scipy
sys.path.append('../../../')
from fonction import *

from fonction import tirage_expo 
print(" TEST TIRAGE EXPONENTIEL ")

np.random.seed(0)

eta, hn, nu, compos = vector_init(list_reac, list_type, vol)
PMC = pmc_init(Nmc, compos, eta)
TAU =[]
for pmc in PMC:
  tau, sig = tirage_expo(list_reac, hn, pmc, list_type, vol, list_sigr)
  TAU.append(tau)
TAU = np.array(TAU)

# reference avec les tirage eponential de numpy: attention 1/sig en argument
ref = np.random.exponential(1./sig, len(PMC))
plt.hist(TAU,30, density = True, alpha = 0.5)
plt.hist(ref,30, density = True, alpha = 0.5)
#plt.show()

print(scipy.stats.kstest(TAU,ref))
#recuperation de la p-value
p_value = scipy.stats.kstest(TAU,ref)[1] 
print(p_value)

if p_value > 0.05:
    print("\n----------\n test OK \n----------\n")
else:
    print("test KO")
    print("\n----------\n test KO \n----------\n")

