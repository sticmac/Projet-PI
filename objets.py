#Lemaire Julien - Casagrande Guillaume - G2
#Module pour les objets.

from turtle import *
from random import *

#Différentes variables gérant la vie (nombre d'habitants encore en vie sur Terre).
vie = 7266000000
vieEnleve = 100000000 #Le nombre de morts à chaque coup.
vieEnleveVirus = 1000000000 #Le nombre de morts à chaque fois qu'on découvre un virus.

#Compte le nombre d'objets différents découverts
nvirus = 0
nantidotes = 0
nbonus = 0

def virus():
    global vie, vieEnleveVirus, nvirus
    write("Virus", False, align="center")
    vie -= vieEnleveVirus
    nvirus += 1

def antidote():
    global vie, vieEnleve, nantidotes
    write("Antidote", False, align="center")
    vie -= vieEnleve
    nantidotes += 1

def bonus():
    global vie, vieEnleve, nbonus
    write("Bonus", False, align="center")
    vieEnleve -= randint(10000,500000)
    vie -= vieEnleve
    nbonus += 1

def plouf():
    global vie, vieEnleve
    write("Plouf !", False, align="center")
    vie -= vieEnleve

def getnvirus():
    return nvirus

def getnantidotes():
    return nantidotes

def getnbonus():
    return nbonus

def getnvie():
    return vie
