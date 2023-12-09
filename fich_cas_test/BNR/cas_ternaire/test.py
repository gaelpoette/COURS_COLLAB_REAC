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
os.system("cp rez.txt rez_mc.txt")
os.system("python3 ode_eps.py")

cmd_gnu="set sty da lp;set grid; set xl 'temps'; set yl 'densite de composants'; plot 'rez_det.txt' w l lt 1 t 'DETER 0', 'rez_mc.txt' w p lt 1 t 'MC 0'"
i=3
for c in range(8):
    if c > 2:
     cmd_gnu+=",'rez_det.txt' u 1:"+str(c)+" w l lt "+str(c)+" t 'DETER "+str(c-2)+"'"
     cmd_gnu+=",'rez_mc.txt'  u 1:"+str(c)+" w p lt "+str(c)+" t 'MC    "+str(c-2)+"'"
cmd_gnu+=";pause -1"
#print cmd_gnu 
output = open("gnu.plot",'w')
output.write(cmd_gnu)
output.close()

os.system("gnuplot gnu.plot")
