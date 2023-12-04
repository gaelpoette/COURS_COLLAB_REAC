def vector_init(list_reac, list_type, vol):
    """ Fonction de remlissage de compos et d'initialisation des vecteurs eta, h et nu"""

    compos=[]
    for i in range(len(list_reac)): 
        compos_reac=(list_reac[i].split(' '))
        for j in range(len(compos_reac)):
            if not(compos_reac[j] in compos):
                compos.append(compos_reac[j])

    print("liste des especes")
    print(compos)

    eta={}
    for c in compos:
        eta[c]=0.
        if c=="Ar" or c=="e^-":
            eta[c] = 1. * vol
        
    print("conditions initiales des espèces")
    print(eta)

    h={}
    nu={}
    for i in range(len(list_reac)):
        print("\n num de reaction = "+str(i)+"")
        reac = list_reac[i]
        compos_reac = (reac.split(' '))
        print(compos_reac)
        # recuperation du vecteur des reactifs
        print("type de reaction: "+list_type[i]+"")

        isnum=0
        if list_type[i] == "binaire":
            h[i] = [compos_reac[0], compos_reac[1]]
        elif list_type[i] == "unaire":
            h[i] = [compos_reac[0]]
        elif list_type[i] == "ternaire":
            h[i] = [compos_reac[0], compos_reac[1], compos_reac[2]]
        else:
            print("type de reaction non reconnue")
            exit(2)

        #recuperation des vecteurs de coefficients stoechiométriques pour chaque reactions
        nu[i]={}
        #print compos
        for cg in compos:
            nu[i][cg] = 0.
            num = 0
            for c in compos_reac:
                isnum=0
                if list_type[i] == "binaire":
                    isnum = (num == 0 or num == 1)
                if list_type[i] == "unaire":
                    isnum = (num == 0)
                if list_type[i] == "ternaire":
                    isnum = (num == 0 or num == 1 or num == 2)
                if c == cg and (isnum): #réactions à 2 réactifs
                    nu[i][cg] += -1.
                if c == cg and (not isnum): #réactions à 2 réactifs
                    nu[i][cg] +=  1.
                else:
                    nu[i][cg] +=  0.
                num+=1
    print("\nles listes de réactifs (h) pour chaque reaction")
    print(h)
    print("les coefficients stoechiométriques (nu) pour chaque reaction")
    print(nu)

    return eta, h, nu, compos


def pmc_init(Nmc, compos, eta):
    """création de la population de particules représentant la condition initiale"""

    PMC=[]
    for nmc in range(Nmc):
        w=1. / Nmc
        eta_nmc={}
        for c in compos:
            eta_nmc[c] = eta[c]
        pmc = {"weight" : w, "densities" : eta_nmc}
        PMC.append(pmc)

    return PMC