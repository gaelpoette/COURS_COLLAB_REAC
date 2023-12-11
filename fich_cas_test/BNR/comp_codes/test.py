#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
from string import *
import os
import random
import matplotlib.pyplot as plt
import numpy as np


print("TEST COMP_CODES")
def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        if f1.read() == f2.read():
            return "The results are identical     : OK"
        else:
            return "The results are not identical : KO"


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

compare_det = compare_files("ref_det.txt", "rez_det.txt")
compare_mc = compare_files("ref_mc.txt", "rez_mc.txt")
print("\n----------\n" + "For rez_det.txt : " + compare_det + "\n----------\n")
print("\n----------\n" + "For rez_mc.txt : "+ compare_mc + "\n----------\n")

# Tracé gnuplot si les fichiers sont différents
if compare_det == "The results are not identical : KO" or compare_mc == "The results are not identical : KO":
    os.system("gnuplot gnu.plot")
