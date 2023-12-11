#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
from string import *
import os
import random
#import sys 
#sys.path.append('./fich_cas_test')
from param import *
import matplotlib.pyplot as plt
import numpy as np
from fonction import * 

random.seed(49)  # Fixe la graine à la valeur 42

# Traiter le cas où les constantes de réaction sont négatives (Jabir)
for i in range (len(list_sigr)):
    if (list_sigr[i]<0):
      print("ATTENTION! Les constantes de reaction doivent etre positif")
      list_sigr[i]= abs(list_sigr[i])
      exit(1)


print("liste des reactions")
print(list_reac)

if (not(len(list_reac)==len(list_sigr))):
  print("ATTENTION! LES LISTES DOIVENT AVOIR LA MEME TAILLE!")
  exit(1)

# Traiter le cas où les constantes de réaction sont négatives (Jabir)
for i in range (len(list_sigr)):
    if (list_sigr[i]<0):
      print("Une des constantes de réaction est négative")
      list_sigr[i]= abs(list_sigr[i])


#"conditions initiales en eta codée en dur pour l'instant
# remlissage de compos et initialisation des vecteurs eta, h et nu
eta, hn, nu, compos = vector_init(list_reac, list_type, vol)

# population de particules représentant la condition initiale
PMC = pmc_init(Nmc, compos, eta)

#entete du fichier
cmd="\n"+"#temps"+" "
for ci in compos:
 cmd+=str(ci)+" "

it=0
tps = 0.
cmd+="\n"+str(tps)+" "
for ci in compos:
 cmd+=str(eta[ci]/vol)+" "

print("\n début du calcul")

while tps < temps_final:

  dt = temps[it+1]-temps[it]

  # initialisation du tableau de tallies
  for ci in compos:
      eta[ci] = 0.

  for pmc in PMC:
    
      tps_cur = 0.

      while tps_cur < dt:

          tau, sig = tirage_expo(list_reac, hn, pmc, list_type, vol, list_sigr)

          # temps courant updaté
          tps_cur += tau

          # détermination de l'évenement que la pmc va subir
          if tps_cur > dt:
              #census
              tps_cur = dt
              for ci in compos:
                  eta[ci] += pmc["densities"][ci] * pmc["weight"]

          else:
            # Fonction de tirages de réactions:
            def reaction(list_reac, hn, list_type, list_sigr, sig):
                U = random.random()

                reac = len(list_reac)-1
                proba = 0.
                for i in range(len(list_reac)-1):
                    prod = 1.
                    for H in hn[i]:
                        prod *= pmc["densities"][H]

                    exposant = 1
                    if list_type[i] == "unaire":
                        exposant = 0
                    elif list_type[i] == "ternaire":
                        exposant = 2
                    volr = vol **exposant
                    proba+= list_sigr[i] / volr * prod

                    if U * sig < proba:
                        reac = i
                        break

                return reac

            reac = reaction(list_reac, hn, list_type, list_sigr, sig) 
            for c in compos:
                  pmc["densities"][c]+=nu[reac][c]         

  tps+=dt
  cmdt=""+str(tps)+" "
  for c in compos:
   cmdt+=str(eta[c] / vol)+" "
  cmd+="\n"+cmdt

output = open("rez.txt",'w')
output.write(cmd)
output.close()


######################### Plot GNU ###################################

if gnuplot:
    cmd_gnu="set sty da l;set grid; set xl 'time'; set yl 'densities of the species'; plot "
    it=3
    cmd_gnu+="'rez.txt' lt 1 w lp  t '"+str(compos[0])+"'"
    for c in compos:
        if not(c==compos[0]):
            cmd_gnu+=",'' u 1:"+str(it)+" lt "+str(it)+" w lp t '"+str(compos[it-2])+"'"
            it+=1

    cmd_gnu+=";pause -1"
    output = open("gnu.plot",'w')
    output.write(cmd_gnu)
    output.close()

    os.system("gnuplot gnu.plot")

######################### Plot Matplotlib ############################

else:
    # Charger les données depuis 'rez.txt'
    data = np.loadtxt('rez.txt')

    # Créer une figure et un axe
    fig, ax = plt.subplots()

    # Configurer l'axe
    ax.set_xlabel('time')
    ax.set_ylabel('densities of the species')
    ax.grid(True)
    # Dessiner chaque colonne de données en tant que série distincte
    for it, c in enumerate(compos):
        ax.plot(data[:, 0], data[:, it+1], 'o-', label=c)

    # Afficher la légende
    ax.legend(loc='best')

    # Enregistrer la figure en tant qu'image
    fig.savefig('output.png')

