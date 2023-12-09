#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from math import *
from string import *
import os
import random


temp_final = 30
dt=1
epsilon = 1.e-4


sig_r_0 = 1.0;
sig_r_1 = 2.0;
sig_r_2 = 0.5;
sig_r_3 = 3.0;

#codage pour dire n+A->B+C et B+C->A+n toujours 2 en entrée seulement
#1
#list_reac={0:"e^- Ar B C", 1:"B C Ar K L"}
#list_type={0:"binaire", 1:"binaire"}
#list_sigr={0:sig_r_0, 1:sig_r_1}
#2
#list_reac={0 : "e^- Ar B C", 1 : "B C Ar K L", 2 : "e^- B C"}
#list_type={0:"binaire", 1:"binaire", 2:"binaire"}
#list_sigr={0 : sig_r_0, 1 : sig_r_1, 2 : sig_r_2}
###3
#list_reac={0 : "e^- Ar e^- e^- Ar^+"}
#list_type={0:"binaire"}
#list_sigr={0 : sig_r_0}
##4
#list_reac={0 : "e^- Ar e^-_s e^-_s Ar^+", 1 : "e^-_s Ar e^-_s e^-_s Ar^+"}
#list_type={0:"binaire", 1:"binaire"}
#list_sigr={0 : sig_r_0, 1 : sig_r_1}
##5
#list_reac={0 : "e^- Ar"}
#list_type={0:"unaire"}
#list_sigr={0 : sig_r_0}
##6
#list_reac={0 : "e^- Ar e^-_s e^-_s Ar^+", 1 : "e^-_s Ar e^-_s e^-_s Ar^+"}
#list_type={0:"binaire", 1:"binaire"}
#list_sigr={0 : sig_r_0, 1 : sig_r_1}
#list_reac={0 : "e^- Ar B C", 1 : "B C Ar K L", 2 : "e^- B C e^-", 3 : "e^- B C e^- e^-"}
#list_type={0:"binaire", 1:"binaire", 2:"binaire", 3:"binaire"}
#list_sigr={0 : sig_r_0, 1 : sig_r_1, 2 : 0.5 * sig_r_2, 3 : 0.5 * sig_r_2}
#list_reac={0 : "e^- Ar B C", 1 : "B C Ar K L", 2 : "e^- B C"}
## PARAM: liste des types de réactions: "binaire" indique qu'il y a 2 réactifs, "unaire" qu'il y en a qu'un seul
#list_type={0:"binaire", 1:"binaire", 2:"binaire"}
## PARAM: la liste des constantes de réactions
#list_sigr={0 : sig_r_0, 1 : sig_r_1, 2 : sig_r_2}
# PARAM: liste des réactions: codage pour dire e^-+Ar->B+C et B+C->Ar+K+L et e^-+B->C
list_reac={0 : "e^- Ar B C", 1 : "B C Ar K L", 2 : "e^- B C", 3: "e^- Ar B C D"}
# PARAM: liste des types de réactions: "binaire" indique qu'il y a 2 réactifs, "unaire" qu'il y en a qu'un seul
list_type={0:"binaire", 1:"binaire", 2:"binaire", 3: "ternaire"}
# PARAM: la liste des constantes de réactions
list_sigr={0 : sig_r_0, 1 : sig_r_1, 2 : sig_r_2, 3 : sig_r_3}


print("liste des reactions")
print(list_reac)

if (not(len(list_reac)==len(list_sigr))):
  print("ATTENTION! LES LISTES DOIVENT AVOIR LA MEME TAILLE!")
  abort


compos=[]
for i in range(len(list_reac)): 
  compos_reac=(list_reac[i].split(' '))
  for j in range(len(compos_reac)):
     if not(compos_reac[j] in compos):
       compos.append(compos_reac[j])

print("liste des densites isotopiques")
print(compos)

#"conditions initiales en eta"
eta={}
for c in compos:
    eta[c]=0.
    if c=="Ar" or c=="e^-":
      eta[c] = 1.
    #if c=="n" :
    #  eta[c] = 0.01


print("conditions initiales en eta")
print(eta)


print("\n")
#eta 0
eta0=eta

#entete du fichier
cmd="\n"+"#temps"+" "
for c in compos:
 cmd+=str(c)+" "


temps = 0.
cmd+="\n"+str(temps)+" "
for c in compos:
 cmd+=str(eta[c])+" "


while temps < temp_final:

  Koef_c={}

  for c in compos:

     Koef = 0.
     for i in range(len(list_reac)):
       reac = list_reac[i]
       compos_reac=(reac.split(' '))

       
       #print c+" est-il réactif ou produit de réaction "+reac+"?"

       #par défaut facteur = 0.
       facteur = 0.
       #print c
       #print compos_reac

       if not(c in compos_reac):
          #alors pas dans la réaction 0.
          facteur = 0.
          #print "absent"
       else:

         facteur = 0.
         num = 0 
         for cg in compos_reac:

           isnum=0
           if list_type[i] == "binaire":
               isnum = (num == 0 or num == 1)
           if list_type[i] == "unaire":
               isnum = (num == 0)

           if c == cg and (isnum):
            #réactif -1
            facteur += -1.
           if c== cg and (not isnum):
            #produit +1
            facteur += +1.
           else:
            facteur +=  0.
           num+=1
            #print "produit"
       #print facteur
       sig_i = list_sigr[i]
       #print "constante de réaction pour"
       #print facteur * sig_i
	   #rappel: deux réactifs maxi => pas d'ambiguité sur le eta0[0] * eta0[1]. De plus, si pas dans reac, sig =0 donc OK
       prod = 0
       if list_type[i] == "binaire":
           prod = eta0[compos_reac[0]] * eta0[compos_reac[1]]
       if list_type[i] == "unaire":
           prod = eta0[compos_reac[0]]

       Koef += facteur * sig_i * prod
       #print Koef 
     Koef_c[c]=Koef

  dt_eps = dt
  for c in compos:
      max_vp = 0.
      if Koef_c[c] == 0.:
        max_vp = 1.e-32
      else:
        max_vp = Koef_c[c]
      dt_eps = min(dt_eps, epsilon/abs(max_vp))

  for c in compos:
     eta[c] = eta0[c] + dt_eps * Koef_c[c]

  temps+=dt_eps
  eta0=eta
  cmd+="\n"+str(temps)+" "
  for c in compos:
   cmd+=str(eta[c])+" "

  #print ""+str(temps)+ " "+str(eta)+" "

#print cmd
output = open("rez_det.txt",'w')
output.write(cmd)
output.close()

cmd_gnu="set sty da lp;set grid; set xl 'temps'; set yl 'densite de composants'; plot 'rez_det.txt' t '"+str(compos[0])+"'"
i=3
for c in compos:
   if not(c==compos[0]):
     cmd_gnu+=",'' u 1:"+str(i)+" t '"+str(compos[i-2])+"'"
     i+=1
cmd_gnu+=";pause -1"
#print cmd_gnu 
output = open("gnu.plot",'w')
output.write(cmd_gnu)
output.close()

#os.system("gnuplot gnu.plot")

