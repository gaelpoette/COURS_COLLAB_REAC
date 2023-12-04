#encapsulage tirage exponentiel aec tau

from math import *
from string import *
import os
import random


# importation des paramètres
from param import *


def tau_func(sig):
#tirage du temps de la prochaine reaction
    U = random.random()
    tau = 1.e32
    if sig > 0.:
        tau = - log(U) / sig
    return tau

