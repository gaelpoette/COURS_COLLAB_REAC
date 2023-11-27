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

# importation des paramètres
if(sig_r_0<0 or sig_r_1<0 or sig_r_2<0):
    print("ATTENTION! Les constantes de reaction doivent etre positif")
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
<<<<<<< HEAD
eta={}
for c in compos:
    eta[c]=0.
    if c=="Ar" or c=="e^-":
      eta[c] = 1. * vol
	
print("conditions initiales des espèces")
print(eta)

# initialisation dess vecteurs list_comp et nu
list_comp, nu = vector_init(list_reac, list_type, compos)
=======
# remlissage de compos et initialisation des vecteurs eta, h et nu
eta, hn, nu, compos = vector_init(list_reac, list_type, vol)
>>>>>>> 726e8b751aa1580ebda3e781eb754f643e8554f7

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

          # section efficace totale
          sig = 0.
          for it in range(len(list_reac)):
              prod = 1.
<<<<<<< HEAD
              for H in list_comp[i]:
                  prod *= pmc["densities"][H]
=======
              for Hi in hn[it]:
                  prod *= pmc["densities"][Hi]
>>>>>>> 726e8b751aa1580ebda3e781eb754f643e8554f7

              exposant = 1
              if list_type[it] == "unaire":
                  exposant = 0
              volr = vol **exposant
              sig+= list_sigr[it] / volr * prod

          #tirage du temps de la prochaine reaction
          Urand = random.random()
          tau = 1.e32
          if sig > 0.:
              tau = - log(Urand) / sig

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
            def reaction(list_reac, h, list_type, list_sigr, sig):
                U = random.random()

<<<<<<< HEAD
              reac = len(list_reac)-1
              proba = 0.
              for i in range(len(list_reac)-1):
                  prod = 1.
                  for H in list_comp[i]:
                      prod *= pmc["densities"][H]
=======
                reac = len(list_reac)-1
                proba = 0.
                for i in range(len(list_reac)-1):
                    prod = 1.
                    for H in h[i]:
                        prod *= pmc["densities"][H]
>>>>>>> 726e8b751aa1580ebda3e781eb754f643e8554f7

                    exposant = 1
                    if list_type[i] == "unaire":
                        exposant = 0
                    volr = vol **exposant
                    proba+= list_sigr[i] / volr * prod

                    if U * sig < proba:
                        reac = i
                        break

                return reac

            reac = reaction(list_reac, h, list_type, list_sigr, sig) 
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

