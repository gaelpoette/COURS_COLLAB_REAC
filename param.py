# PARAM: nb de particules MC
Nmc=10
# PARAM: Volume
vol = 10.
# PARAM: construction de la liste des temps d'intérêt
temps_final = 30
dt=1
Nt = int(temps_final/dt)
temps=[]
t=0.
for it in range(Nt):
    temps.append(t)
    t+=dt

# PARAM: liste des réactions: codage pour dire e^-+Ar->B+C et B+C->Ar+K+L et e^-+B->C
list_reac={0 : "e^- Ar B C", 1 : "B C Ar K L", 2 : "e^- B C"}
# PARAM: liste des types de réactions: "binaire" indique qu'il y a 2 réactifs, "unaire" qu'il y en a qu'un seul
list_type={0:"binaire", 1:"binaire", 2:"binaire"}
# les constantes des réactions
sig_r_0 = 1.0;
sig_r_1 = 2.0;
sig_r_2 = 0.5;
# PARAM: la liste des constantes de réactions
list_sigr={0 : sig_r_0, 1 : sig_r_1, 2 : sig_r_2}

# PARAM MANQUANT: pour l'instant, la liste des conditions initiales est en dur...
# pour comprendre comment elles sont codées, faut regarder...
