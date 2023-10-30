def vector_init(list_reac, list_type, compos):
    """ Fonction d'initialisation des vecteurs h et nu"""
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

    return h, nu


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