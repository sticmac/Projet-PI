#Lemaire Julien - Casagrande Guillaume - G2
#Module pour les objets.

from turtle import *
from random import *

#Différentes variables gérant la vie (nombre d'habitants encore en vie sur Terre).
nvie = 7266000000
vieEnleve = 100000000 #Le nombre de morts à chaque coup.
vieEnleveVirus = 1000000000 #Le nombre de morts à chaque fois qu'on découvre un virus.

#Compte le nombre d'objets différents découverts
nvirus = 0
nantidotes = 0
nbonus = 0

score = 0

def virus():
    global nvie, vieEnleveVirus, nvirus
    write("Virus", False, align="center")
    nvie -= vieEnleveVirus
    nvirus += 1

def antidote():
    global nvie, vieEnleve, nantidotes, score
    write("Antidote", False, align="center")
    score += 100
    nvie -= vieEnleve
    nantidotes += 1

def bonus():
    #Un bonus peut avoir deux effets :
    #Soit il diminue le nombre de morts par tour, soit il augmente le score
    global nvie, vieEnleve, nbonus, score
    categorie = randint(0,1) #Pioche le bonus de vie (0) ou le bonus de score (1)
    if categorie == 0:
        vieEnleve -= randint(1000000,6000000)
        write("Bonus de vie", False, align="center")
    else:
        score += randint(10,200)
        write("Bonus de score", False, align="center")
    nvie -= vieEnleve
    nbonus += 1

def plouf():
    global nvie, vieEnleve
    write("Plouf !", False, align="center")
    nvie -= vieEnleve

def getscore():
    return score

def getnvirus():
    return nvirus

def getnantidotes():
    return nantidotes

def getnbonus():
    return nbonus

def getnvie():
    return nvie

def setscore(nvscore):
    global score
    score = nvscore

def setnvirus(virus):
    global nvirus
    nvirus = virus

def setnantidotes(antidotes):
    global nantidotes
    nantidotes = antidotes

def setnbonus(bonus):
    global nbonus
    nbonus = bonus

def setnvie(vie):
    global nvie
    nvie = vie
    
